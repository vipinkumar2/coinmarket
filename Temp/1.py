from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Riken\Desktop\coinmarket\profiles") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=004')
options.add_argument('--no-sandbox')
options.add_argument('--autoplay-policy=no-user-gesture-required')
options.add_argument('--start-maximized')    
options.add_argument("--ignore-certificate-errors")
options.add_argument("--enable-javascript")
options.add_argument("--disable-notifications")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--enable-popup-blocking")
options.add_argument("--ignore-certificate-errors-spki-list")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://yopmail.com/en/email-generator')

# driver.get('https://coinmarketcap.com/')

def new_tab(link='www.google.com'):
    driver.execute_script(f"window.open('{link}')")
    driver.switch_to.window(driver.window_handles[-1]) 

new_tab('https://coinmarketcap.com/')
input('Enter :')
driver.quit()
