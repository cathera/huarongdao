from PIL import Image
import sys
from random import randint

def Get_divided(img):
    return 6,6


#Read image
original_image=Image.open("test.jpg")
blank=Image.open("blank.jpg")
#Divide image
region=Get_divided(original_image)
w_sep,h_sep=int(original_image.size[0]/region[0]),int(original_image.size[1]/region[1])
divided_image=[original_image.crop((a*w_sep,b*h_sep,a*w_sep+w_sep,b*h_sep+h_sep)) for a in range(0,region[0]) for b in range (0,region[1])]
mixed_divided_img=[]
mix_num=len(divided_image)-1
blank=blank.crop((0,0,w_sep,h_sep))
for i in range(0,mix_num):
    mixed_divided_img.append(divided_image.pop(randint(1,mix_num-i)))
mixed_image=original_image.copy()
for a in range(0,region[0]):
    for b in range(0,region[1]):
        try:
            mixed_image.paste(mixed_divided_img.pop(),(a*w_sep,b*h_sep))
        except IndexError as err:
            mixed_image.paste(blank,(a*w_sep,b*h_sep,a*w_sep+w_sep,b*h_sep+h_sep))
            mixed_image.save("mixed.jpeg")


#Restore image