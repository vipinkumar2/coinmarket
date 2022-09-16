import base64
import json                    

import requests

api = 'http://3.110.38.186:8082/captcha_resolver/'
# image_file = 'C:\Users\Riken\Desktop\coinmarket\captcha_image.png'

with open('C:\Users\Riken\Desktop\coinmarket\captcha_image.png', "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")
param = { 
        "file": im_b64
        }
r = requests.post(url=api,params=param)
print(r.text)
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
# payload = json.dumps({"image": im_b64, "other_key": "value"})
# response = requests.post(api, data=payload, headers=headers)
# try:
#     data = response.json()     
#     print(data)                
# except requests.exceptions.RequestException:
#     print(response.text)