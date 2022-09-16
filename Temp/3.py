import requests # request img from web
import shutil # save img locally

url = 'https://staticrecap.cgicgi.io/image/antibot/BOX/captcha/20220715/05/303b14757106434ea400625d6b9570ef.jpeg' #prompt user for img url
file_name = '12121.png' #prompt user for file_name

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')