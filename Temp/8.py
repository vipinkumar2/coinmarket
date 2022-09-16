import requests
from PIL import Image

from pathlib import Path
CAPTCHA_URL = 'http://3.110.38.186:8082/captcha_resolver/'
images_path = Path.cwd() / 'captcha_images/cutted_images/captcha_images7.png'
# images_path = 'C:\Users\Riken\Desktop\coinmarket\captcha_images\cutted_images\captcha_images6.png'
print(images_path)

def get_identification():   

    # for i in range(9):


    image = images_path.open(mode='rb')
    rrr = requests.post(CAPTCHA_URL,files={'file' : image})
    print(rrr.text)
    

def crop_image():
    full_img = Image.open('C:\\Users\\Riken\\Desktop\\coinmarket\\captcha_images/cutted_images/captcha_images9.png')
    full_img.show()
    # width,height = full_img.size
    # print(width,":",height)
    ...
get_identification()
# crop_image()


'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"moped","root_class":""}'
'{"actual_class":"schooner","root_class":"ship"}'
'{"actual_class":"mountain_bike","root_class":"bicycle"}'
'{"actual_class":"mountain_bike","root_class":"bicycle"}'
'{"actual_class":"recreational_vehicle","root_class":""}'
'{"actual_class":"pirate","root_class":"ship"}'
'{"actual_class":"lumbermill","root_class":""}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"space_shuttle","root_class":""}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"toaster","root_class":""}'
'{"actual_class":"killer_whale","root_class":""}'
'{"actual_class":"car_wheel","root_class":""}'
'{"actual_class":"limousine","root_class":"car"}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"liner","root_class":"ship"}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"fireboat","root_class":"ship"}'
'{"actual_class":"guillotine","root_class":""}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"minibus","root_class":"bus"}'
'{"actual_class":"school_bus","root_class":"bus"}'
'{"actual_class":"prison","root_class":""}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"airliner","root_class":"airplane"}'
'{"actual_class":"drilling_platform","root_class":""}'
'{"actual_class":"sports_car","root_class":"car"}'
'{"actual_class":"mountain_bike","root_class":"bicycle"}'
'{"actual_class":"mountain_bike","root_class":"bicycle"}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"space_shuttle","root_class":""}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"theater_curtain","root_class":""}'
'{"actual_class":"container_ship","root_class":"ship"}'
'{"actual_class":"amphibian","root_class":"car"}'
'{"actual_class":"speedboat","root_class":"ship"}'
'{"actual_class":"projectile","root_class":""}'
'{"actual_class":"window_shade","root_class":""}'
'{"actual_class":"moving_van","root_class":""}'
'{"actual_class":"airliner","root_class":"airplane"}'
'{"actual_class":"bicycle-built-for-two","root_class":"bicycle"}'
'{"actual_class":"space_shuttle","root_class":""}'

'{"actual_class":"Great_Dane","root_class":"dog"}'
'{"actual_class":"golden_retriever","root_class":""}'
'{"actual_class":"toucan","root_class":"bird"}'
'{"actual_class":"hummingbird","root_class":"bird"}'
'{"actual_class":"Labrador_retriever","root_class":""}'
'{"actual_class":"giant_panda","root_class":"panda"}'
'{"actual_class":"jacamar","root_class":"bird"}'
'{"actual_class":"Rhodesian_ridgeback","root_class":"dog"}'
'{"actual_class":"Blenheim_spaniel","root_class":"dog"}'