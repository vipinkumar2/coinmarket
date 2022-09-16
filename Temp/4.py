        
from PIL import Image


def crop_images():
    from PIL import Image
    full_img = Image.open('etc\captcha_image.png')
    width,height = full_img.size
    print(width,":",height)
    onethird_height = inner_h= height/3
    onethird_width =inner_w = width/3
    a= []
    b = []
    uper_height = 0
    uper_width = 0
    for i in range(3):
        i_cropped_img = full_img.crop((0,uper_height,width,inner_h))
        uper_height += onethird_height
        inner_h += onethird_height
        i += 1
        i_cropped_img.show()
        # image_path = f'C:\Users\Riken\Desktop\coinmarket\etc\captcha_image.png'
        iii = open(f"C:\Users\Riken\Desktop\coinmarket\etc\3combo_captcha_images\combo_{i}.png", "a")
        i_cropped_img.save(iii)
        # i_cropped_img.show()
        print(i_cropped_img)
        
        a.append(i_cropped_img)
        ...
    for i_a in a:
        for i_n in range(3):
            i_n = i_a.crop((uper_width,0,inner_w,height))
            uper_width += onethird_width
            inner_w += onethird_width
            print('------------------')
            i_n.show()

crop_images()


















# def crop_images():
#     from PIL import Image
#     full_img = Image.open('etc\captcha_image.png')
#     width,height = full_img.size
#     print(width,":",height)
#     # full_img.show()
#     # cropped = full_img.crop((0,0,width/3,height/3))  # 1
#     # cropped.show()
#     # cropped = full_img.crop((width/3,0,(width/3)*2,height/3))  # 2
#     # cropped.show()
#     # cropped = full_img.crop(((width/3)*2,0,width,height/3)) # 3
#     # cropped.show()
#     # cropped = full_img.crop((0,width/3,width/3,(height/3)*2)) # 4
#     # cropped.show()
#     cropped = full_img.crop(((width/3)*2,0,width,height/3)) # 5
#     cropped.show()
#     # cropped = full_img.crop(((width/3)*2,0,width,height/3)) # 6
#     # cropped.show()
#     # cropped = full_img.crop(((width/3)*2,0,width,height/3)) # 7
#     # cropped.show()
#     # cropped = full_img.crop(((width/3)*2,0,width,height/3)) # 8
#     # cropped.show()
#     # cropped = full_img.crop(((width/3)*2,0,width,height/3)) # 9
#     # cropped.show()
# crop_images()