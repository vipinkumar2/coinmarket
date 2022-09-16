import requests, shutil # save img locally
from pathlib import Path

image_captcha_url = 'https://source.unsplash.com/1600x900?ship'
count = 0
IMAGE_FOLDER = Path.cwd() / 'zzzz/cars/1.txt'



for i in range(72,1000):
    Captcha_img_file_name = Path.cwd() / f'zzzz/ship/ship_{i}.png'
    res = requests.get(image_captcha_url, stream = True)
    with open(Captcha_img_file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)

    
    print(i)

    # input('Enter :')
                                    