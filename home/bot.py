from enum import Flag
import json
from lib2to3.pgen2 import driver
from pprint import pprint
from tkinter.messagebox import RETRY
from urllib import response
from driver.driver import get_driver
import time, random, logging, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from CMC.settings import BASE_DIR, LOGGER
from home.models import comments, user_details
from home.utils import COMMENTS_LI, random_sleep
import requests
from pathlib import Path
import requests # request img from web
import shutil # save img locally
from selenium.webdriver.common.action_chains import ActionChains

# variables
CAPTCHA_URL = 'http://3.110.38.186:8082/captcha_resolver/'
IMAGE_FOLDER = Path.cwd() / 'captcha_images'
class coinmarket:

    def __init__(self,profile_dir = 'profile',hide_browser = False) -> None:
        self.user = ''
        if profile_dir != 'profile':
            if not user_details.objects.filter(profile_name = profile_dir).exists() :
                self.user = user_details.objects.create(
                    profile_name = profile_dir,
                )
            else:
                self.user = user_details.objects.filter(profile_name = profile_dir).first()

        self.logger = LOGGER
        self.logger.info('Driver is genrated !')
        self.driver = get_driver(profile_dir=profile_dir,hide_browser=hide_browser)
        print(self.driver)
        random_sleep(5,10,reason='open driver')
        self.action = ActionChains(self.driver)
        self.email = self.user.email
        self.image_captcha_url = ''
        self.three_plates_images_path = []
        self.all_cutted_captcha_images = []
        self.captcha_image_links = []
        self.captcha_image_path = []
        self.captcha_link_divs = ''
        self.Captcha_img_file_name = os.path.join(BASE_DIR, f'captcha_images/captcha_image{self.user.profile_name}')
        

    def sign_up(self):
        self.driver.get('https://coinmarketcap.com/')
        sign_up_btn = False
        profile_img = False
        self.new_tab(refresh_needed=True)
        self.switch_tab('-1')
        self.give_new_email()

        self.switch_tab(0)

        for i in range(5):
            self.driver.refresh()
            random_sleep(2,5)

            profile_img = self.find_element('profile pic','avatar-img',By.CLASS_NAME)
            if profile_img :
                self.logger.info('The user is alrady logged in')
                return True

            # to close pop which is comming in starting
            self.close_startup_popup()
            

            sign_up_btn = self.click_element('signup btn','//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/button[2]',By.XPATH)
            if sign_up_btn == False:
                self.logger.info('There is not sign up btn')
                break

            # self.driver.refresh()

            # input email and password in signup fields
            random_sleep()
            inputs = self.driver.find_elements(By.CLASS_NAME,'dqGVRN')
            for  inp in inputs:
                try:
                    if inp.get_attribute('type') == 'email' :inp.send_keys(self.email)
                    if inp.get_attribute('type') == 'password' :inp.send_keys(str(self.email).capitalize())
                except Exception as e: ...

            random_sleep()
            for i in range(3):
                self.click_element('create an account btn','dKttWP',By.CLASS_NAME)
                random_sleep()
                if self.find_element('open captcha model','bs-modal',By.CLASS_NAME,timeout=0) :break
                if self.find_element('open image classification captcha','bcap-modal',By.CLASS_NAME,timeout=0):
                    # self.find_element('open image classification captcha','/html/body/div[4]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div',By.XPATH,timeout=0).get_attribute("style")
                    self.solving_captcha()
                    # input('Enter after you solve the captcha :')

                    self.click_element('open verification input','/html/body/div[3]/div/div/div/div/div[3]/div/div[3]/span',By.XPATH)
                    self.verify_email()
                    self.driver.refresh()
                    self.driver.refresh()
                    self.driver.refresh()
                    is_user_loggedIn = self.check_login()
                    if is_user_loggedIn:
                        self.user.status = 'ACTIVE'
                        self.user.save()
                    return is_user_loggedIn
    
    def login(self):
        self.driver.get('https://coinmarketcap.com/')
        is_user_login = self.check_login()
        self.close_startup_popup()

        self.logger.info(f'the is login : {is_user_login}------------')

        # login the user if it is not

        for i in range(3):
            is_user_login = self.check_login()  
            if is_user_login == True : break
            if is_user_login == False :
                self.click_element('login btn','latwGv',By.CLASS_NAME)
                random_sleep(reason='to open login menu')


                # input email and password in signup fields
                random_sleep()
                inputs = self.driver.find_elements(By.CLASS_NAME,'dqGVRN')
                for  inp in inputs:
                    try:
                        if inp.get_attribute('type') == 'email' :inp.send_keys(self.email)
                        if inp.get_attribute('type') == 'password' :inp.send_keys(str(self.email).capitalize())
                    except Exception as e: ...

                self.click_element('Login btn','dKttWP',By.CLASS_NAME)

                if self.find_element('open image classification captcha','bcap-modal',By.CLASS_NAME):
                    
                    self.solving_captcha()
                    
                random_sleep()
                self.driver.refresh()

    def comment_on_xana(self):
        while True :
            self.driver.get('https://coinmarketcap.com/currencies/xana/')
            action = ActionChains(driver)
            random_sleep(reason='comment box')
            # input('Enter :1')
            scroll_to_comment = self.find_element('scroll comment','name-section',By.CLASS_NAME)
            scroll_to_comment_location = scroll_to_comment.location
            self.driver.execute_script(f"window.scrollBy({scroll_to_comment_location['x']},{scroll_to_comment_location['y']});")
            # input('Enter :2')
            self.driver.find_element(By.XPATH,'//*[@id="cmc-editor"]/div/div[1]/div/span/span[1]').click()
            # input('Enter :3')
            random_comment = random.choice(COMMENTS_LI)

            try:
                comment_bb = self.driver.find_element(By.XPATH,'//*[@id="cmc-editor"]/div/div[2]/div/div/p/span[3]/span/span')
                comment_bb.send_keys(random_comment)
            except Exception as e: 
                print(e,'----comment box send keys')
            query_sector_of_comment_inbox = f'document.querySelector("#cmc-editor > div > div.sc-1pyr0bh-0.sc-1u9rs9p-1.dBQPvF.gravity > div > div > p > span:nth-child(3) > span > span").innerText = " {random_comment}" '
            self.driver.execute_script(query_sector_of_comment_inbox)
            # input('Enter :4')
            self.click_element('comment post btn','iXyGdC',By.CLASS_NAME)
            # input('Enter :5')
            random_sleep(reason='let post sent')
            comments.objects.create(
                user = self.user,
                comment = random_comment
            )
            try:
                repeatation = input('Enter check after posts commnet \n1 for repeat process or\n2 for complete process:')
                if int(repeatation) == 2:
                    break
            except Exception as e: 
                print(e)

    def close_startup_popup(self):
        '''to close pop up for search suggestion if it is exists '''
        try:self.driver.execute_script("document.getElementsByClassName('HBft')[1].click()")
        except Exception as e: ...

    def solving_captcha(self):
        self.save_images_of_captcha()
        from PIL import Image
        self.logger.info('Trying to solve the captcha')
        self.crop_captcha_images()
        require_captcha_image = str(self.getvalue_byscript('document.querySelector("#tagLabel").innerText')).strip()
        
        image___count = 0
        next_btn_clicked = False
        for image  in range(18):
            time.sleep(0.5)
            image_path = Path.cwd() / f'captcha_images/cutted_images/captcha_images{image+1}.png'
            image = image_path.open(mode='rb')
            responses = requests.post(CAPTCHA_URL,files={'file' : image})
            response_json = json.loads(responses.text)
            if require_captcha_image == response_json['response'].strip() :
                self.captcha_link_divs[image___count].click()
            image___count +=1
            if image___count >= 9 and next_btn_clicked == False:
                self.click_element('captcha Next btn','bcap-verify-button',By.CLASS_NAME)
                next_btn_clicked = True
        # input('Enter ')
        self.click_element('captcha Next btn','bcap-verify-button',By.CLASS_NAME)

    def check_login(self):
        self.driver.get('https://coinmarketcap.com/')
        profile_img = self.find_element('profile pic','avatar-img',By.CLASS_NAME)
        if profile_img :
            self.logger.info('The user is alrady logged in')
            return True
        else:
            return False
    
    
    def crop_captcha_images(self):
        from PIL import Image
            
        for captcha_images in self.captcha_image_path :
            full_img = Image.open(captcha_images)
            width,height = full_img.size

            onethird_height = inner_h= height/3
            onethird_width =inner_w = width/3

            uper_height = 0
            uper_width = 0
            for i in range(3):
                i_cropped_img = full_img.crop((0,uper_height,width,inner_h))
                uper_height += onethird_height
                inner_h += onethird_height
                i += 1
                image_path = str(IMAGE_FOLDER) + f'/three_plates/captcha_images{int(self.captcha_image_path.index(captcha_images))+1}' +str(i)+'.png'
                self.three_plates_images_path.append(image_path)
                i_cropped_img.save(image_path)

        captcha_images_count = 0
        for image in self.three_plates_images_path :
            image = Image.open(image)
            width,height = image.size
            onethird_height = inner_h= height/3
            onethird_width =right_w = width/3
            uper_height = 0
            left_w = 0

            for i in range(3):
                image_cuted = image.crop((left_w,0,right_w,height))    
                # image_cuted.show()
                right_w += onethird_width
                left_w += onethird_width
                captcha_images_count += 1
                cutted_image_path = str(IMAGE_FOLDER) + '/cutted_images/captcha_images' +str(captcha_images_count)+'.png'
                self.all_cutted_captcha_images.append(cutted_image_path)
                image_cuted.save(cutted_image_path)

    def pp_get_verification(self):
        random_sleep()
        self.driver.get('https://yopmail.com/en/wm')
        random_sleep(3,5)

        self.driver.switch_to.frame('ifmail')
        links = self.driver.find_element(By.XPATH,'//*[@id="mail"]/div/div/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[7]/td/span/a').get_attribute('href')
        self.driver.get(links)

    def verify_email(self):
        self.switch_tab(-1)
        # self.click_element('open inbox','/html/body/div/div[2]/main/div/div[2]/div/div/div[2]/button[2]',By.XPATH)
        random_sleep(5,9)
        self.driver.get('https://yopmail.com/en/')
        self.input_text(self.email,'get email inbox input','ycptinput',By.CLASS_NAME)
        self.click_element('go to email inboc btn','refreshbut',By.ID)
        self.click_element('go to email inboc btn2','//*[@id="refreshbut"]/button',By.XPATH)
        self.click_element('open inbox','/html/body/div/div[2]/main/div/div[2]/div/div/div[2]/button[2]',By.XPATH)
        random_sleep(5,9)
        # self.driver.get('https://yopmail.com/en/')
        self.driver.switch_to.frame('ifmail')
        links = self.driver.find_element(By.XPATH,'//*[@id="mail"]/div/div/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[7]/td/span/a').get_attribute('href')
        self.driver.get(links)

    def profile_update(self,):
        self.driver.get('https://coinmarketcap.com/')
        if self.check_user_login():
            self.logger.info('Now script can go further')
            self.open_profile()
            self.click_element('Edit btn','himhHq',By.CLASS_NAME)
            random_sleep(3,5)
            self.click_element('profile pic update','cczexb',By.CLASS_NAME)
            random_sleep()
            profile_pics = self.driver.find_elements(By.CLASS_NAME,'blGGlc')
            first_profile_pic = profile_pics.pop(0)
            last_profile_pic = profile_pics.pop(-1)
            random.choice(profile_pics).click()
            self.click_element('confirm to selected profile pic btn','cJcdZL',By.CLASS_NAME)
            self.input_text()

        else:
            # we need to add a system to login if user is not logged in
            self.logger.info('Please try to login and then try to update the profile')
        ...

    def check_user_login(self):
        profile_img = self.find_element('profile pic','avatar-img',By.CLASS_NAME)
        if profile_img :
            self.logger.info('The user is alrady logged in')
            return True
        else:return False

    def save_images_of_captcha(self):
        
            
        self.captcha_image_links = []
        random_sleep()
        self.captcha_link_divs = self.driver.find_elements(By.CLASS_NAME,'bcap-image-cell-image')
        if self.captcha_link_divs :
            for captcha_div in self.captcha_link_divs :
                divs_style = captcha_div.get_attribute('style')
                if 'https' in divs_style :
                    divs_style = divs_style.strip().split('"')
                    for style_link in divs_style :
                        if 'https' in style_link :
                            if not style_link in self.captcha_image_links :
                                self.captcha_image_links.append(style_link)
        
        
        for image_link in self.captcha_image_links :
            res = requests.get(image_link, stream = True)
            if res.status_code == 200:
                with open(f'{self.Captcha_img_file_name}_{self.captcha_image_links.index(image_link)}.jpeg','wb') as f:
                    shutil.copyfileobj(res.raw, f)
                    self.captcha_image_path.append(f'{self.Captcha_img_file_name}_{self.captcha_image_links.index(image_link)}.jpeg')
                    self.logger.info(f'Image sucessfully Downloaded: {self.Captcha_img_file_name}_{self.captcha_image_links.index(image_link)}.jpeg')
            else:
                self.logger.info(f"Image Couldn't be retrieved at path : {self.Captcha_img_file_name}_{self.captcha_image_links.index(image_link)}.jpeg")

    def give_new_email(self):
        self.driver.get('https://yopmail.com/en/email-generator')
        # random_sleep(4,8)
        self.find_element('email','egen',By.ID)
        genrated_email = self.getvalue_byscript('document.querySelector("#egen").innerText')
        self.logger.info(f'New Genrated email : {genrated_email} ')
        self.email = genrated_email
        self.user.email = str(genrated_email)
        self.user.password = str(genrated_email).capitalize()
        self.user.save()
        return genrated_email

    def open_profile(self):
        profile_btn = False
        avatar_img = self.find_element('profile pic','avatar-img',By.CLASS_NAME)
        if avatar_img :
            self.action.move_to_element(avatar_img).perform()
            profile_btn = self.click_element('click to profile btn','//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/a',By.XPATH)
        return True if profile_btn != False else False
        
    def follow_user(self,user_link=''):
        """it will follow the user of which user's link is given else it will return false"""
        follow_btn = False
        self.open_profile()
        self.driver.refresh()
        self.driver.get(user_link)
        if user_link != "":
            random_sleep(4,7)
            follow_btn = self.click_element('Follow btn','eyPPna',By.CLASS_NAME)
        return True if follow_btn != False else False

    def new_tab(self,link='www.google.com',refresh_needed = False):
        """open a new tab and open link which is given else it will open google search bar"""
        self.driver.execute_script(f"window.open('{link}')")
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        if refresh_needed :self.driver.refresh()

    def switch_tab(self,index=0,**link):
        """switch to tab by index starting from 0"""
        self.driver.switch_to.window(self.driver.window_handles[int(index)]) 

    def getvalue_byscript(self,script = ''):
        """made for return value from ele or return ele"""
        value = self.driver.execute_script(f'return {script}')
        return value

    def quite_driver(self):
        """close the driver"""
        try:self.driver.quit()
        except Exception as e:print(e)
            
        

    def find_element(self, element, locator, locator_type=By.XPATH,
            page=None, timeout=10,
            condition_func=EC.presence_of_element_located,
            condition_other_args=tuple()):
        """Find an element, then return it or None.
        If timeout is less than or requal zero, then just find.
        If it is more than zero, then wait for the element present.
        """
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                ele = wait_obj.until(
                        condition_func((locator_type, locator),
                            *condition_other_args))
            else:
                self.logger.info(f'Timeout is less or equal zero: {timeout}')
                ele = self.driver.find_element(by=locator_type, 
                        value=locator)
            if page:
                self.logger.info(
                        f'Found the element "{element}" in the page "{page}"')
            else:
                self.logger.info(f'Found the element: {element}')
            return ele
        except (NoSuchElementException, TimeoutException) as e:
            if page:
                self.logger.info(f'Cannot find the element "{element}"'
                        f' in the page "{page}"')
            else:
                self.logger.info(f'Cannot find the element: {element}')
            
            return False

    def click_element(self, element, locator, locator_type=By.XPATH,
            timeout=10,page=None):
        
        """Find an element, then click and return it, or return None"""
        try:
            ele = self.find_element(element, locator, locator_type, timeout=timeout,page=page)
            if ele:
                ele.click()
                self.logger.info(f'Clicked the element: {element}')
                return ele

            else:return False
        except Exception as e:self.logger.info(e)

    def input_text(self, text, element, locator, locator_type=By.XPATH,
            timeout=10, page=None):
        
        """Find an element, then input text and return it, or return None"""
        try:
            
            ele = self.find_element(element, locator, locator_type=locator_type,
                    timeout=timeout,page=page)
            if ele:
                ele.clear()
                ele.send_keys(text)
                self.logger.info(f'Inputed "{text}" for the element: {element}')
                return ele
        except Exception as e :
            self.logger.info(f'Got an error in input text :{element} {e}')
            
            return False

