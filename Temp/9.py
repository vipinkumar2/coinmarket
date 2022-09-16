

import json
import requests
from PIL import Image

from pathlib import Path

images_path = Path.cwd() / 'captcha_images'




import requests
from PIL import Image

from pathlib import Path
captcha_img_number = 'captcha_image13'
# captcha_img_number = 'f78a022e8ef54f1cb203ccf001990f84'
images_path = Path.cwd() / 'captcha_images'
a = []
print(images_path)
def crop_image():

    full_img = Image.open(f'captcha_images/{captcha_img_number}.jpeg')
    # full_img = Image.open(f'captcha_images/captcha_image{captcha_img_number}.jpeg')
    width,height = full_img.size
    print(width,":",height)

    onethird_height = inner_h= height/3
    onethird_width =inner_w = width/3

    three_plates_images_path = []
    uper_height = 0
    uper_width = 0
    for i in range(3):
        i_cropped_img = full_img.crop((0,uper_height,width,inner_h))
        uper_height += onethird_height
        inner_h += onethird_height
        i += 1
        image_path = str(images_path) + '/three_plates/captcha_images' +str(i)+'.png'
        three_plates_images_path.append(image_path)
        # i_cropped_img.show()
        i_cropped_img.save(str(images_path) + '/three_plates/captcha_images' +str(i)+'.png')


    captcha_images_count = 0
    for image in three_plates_images_path :
        image = Image.open(image)
        width,height = image.size
        onethird_height = inner_h= height/3
        onethird_width =right_w = width/3
        three_plates_images_path = []
        uper_height = 0
        left_w = 0

        for i in range(3):
            image_cuted = image.crop((left_w,0,right_w,height))    
            # image_cuted.show()
            right_w += onethird_width
            left_w += onethird_width
            captcha_images_count += 1

            img__path = str(images_path) + f'/cutted_images/{captcha_img_number}_' +str(captcha_images_count)+'.png'
            a.append(img__path)
            image_cuted.save(img__path)
            # image_cuted.show()
crop_image()

images_path = Path.cwd() / 'captcha_images'
CAPTCHA_URL = 'http://3.110.38.186:8082/captcha_resolver/'
captcha_images_count = 1
for i in range(1,10):
    with open(f'/home/riken/Desktop/workplace/COINMARKET/coinmarket/captcha_images/cutted_images/{captcha_img_number}_{i}.png', "rb") as image:
        f = image.read()
        b = bytearray(f)
        rrr = requests.post(CAPTCHA_URL,files={'file' : f})
        # print(type(rrr.text))
        rrr = json.loads(rrr.text)
        print(rrr['response'].strip())