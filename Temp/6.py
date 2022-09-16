URL = 'http://3.110.38.186:8082/captcha_resolver/'
import cv2 as cv
import base64


img = cv.imread(r'84a87e74b5b3432bb8f33721853bd803_8.jpg')
import requests
# img = base64.b64encode(img).decode("utf8")
param = { 
        "file": img
        }

r = requests.post(url=URL,data=param)
print(r.text)