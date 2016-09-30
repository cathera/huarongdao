from PIL import Image
import sys
from random import randint

def Get_divided(img):
    return 6,6

def RGB_match(line_RGB_tuple_1,line_RGB_tuple_2):
    match_count=0
    match_value=6
    width=min((len(line_RGB_tuple_1),len(line_RGB_tuple_2)))
    for i in range(0,width):
        match_count+=(abs(line_RGB_tuple_1[i][0]-line_RGB_tuple_2[i][0]<match_value) and abs(line_RGB_tuple_1[i][1]-line_RGB_tuple_2[i][1]<match_value and abs(line_RGB_tuple_1[i][2]-line_RGB_tuple_2[i][2]<match_value)))
    return match_count/width
def is_beside(img1,img2):
    #Returns:
    # L for img2 is on the left side of img1
    # R
    # U
    # D
    # N for img2 is not beside img1
    #RGB_tuple: 10 sample points from L, R, U , D
    RGB_tuples_1={}
    #Corresponding side for L, R, U, D
    RGB_tuples_2={}
    for side in RGB_tuples_1.keys():
        if RGB_match(RGB_tuples_1[side],RGB_tuples_2[side]):
            return side
    return 'N'

def get_side_RGB(img):
    global w_sep,h_sep
    all_data=list(img.getdata())
    left=[tuple for tuple in all_data[:w_sep]]
    right=[tuple for tuple in all_data[-w_sep:]]
    up=[tuple for tuple in all_data[::w_sep]]
    down=[tuple for  tuple in all_data[w_sep::w_sep]]
    return (left,up,right,down)

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
    #mixed_divided_img.append(divided_image.pop(randint(1,mix_num-i)))
    mixed_divided_img.append(divided_image.pop(0))
color_set=[]
for img in mixed_divided_img:
    color_set.append(get_side_RGB(img))
mixed_divided_img[0].show()
#mixed_divided_img[1].show()
print (RGB_match(color_set[0][3],color_set[1][1]))
mixed_image=original_image.copy()
for a in range(0,region[0]):
    for b in range(0,region[1]):
        try:
            mixed_image.paste(mixed_divided_img.pop(),(a*w_sep,b*h_sep))
        except IndexError as err:
            mixed_image.paste(blank,(a*w_sep,b*h_sep,a*w_sep+w_sep,b*h_sep+h_sep))
            mixed_image.save("mixed.jpeg")
#Restore image