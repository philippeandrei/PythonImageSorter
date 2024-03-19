from colorthief import ColorThief
import scipy.spatial as sp
import matplotlib.pyplot as plt
import json
import os
from os import listdir
import math
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
import time
import threading




photo_labels = []
start_time = time.time()

def show_images(image_paths, color):

    win = tk.Toplevel()
    win.title(color)
    print(color)
    COLUMNS = 25
    image_count = 0
    for image in image_paths:
        if(image_count > 200):
            break
        image_count += 1
        r, c = divmod(image_count - 1, COLUMNS)
        im = Image.open(image)
        resized = im.resize((90, 90))
        tkimage = ImageTk.PhotoImage(resized)
        myvar = tk.Label(win, image=tkimage)
        myvar.image = tkimage
        myvar.grid(row=r, column=c)
    win.mainloop()  # Not sure if you need this, too, or not...



def clear_photos():
    for label in photo_labels:
        label.destroy()
    photo_labels.clear()
def distance(x1, y1, z1, x2, y2, z2):
    d = 0.0
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return d

def get_pallete(path):
    color_thief = ColorThief(path)
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=5, quality=1)

    color_palette = []
    for color in palette:
        if color[5] != 0.0:
            color_palette.append({"color": color[:3], "percentage": color[5]})

    color_palette = sorted(color_palette, key=lambda d: d['percentage'], reverse=True)

    palette = []
    for p in color_palette:
        palette.append(p['color'])

    # print("Color Palette : ")
    # print(color_palette)
    # print(palette)
    return color_palette
def write(my_data):
    with open('data.json', 'w') as file:
        json.dump(my_data, file)


def main(color_to_find):
    with open('data.json', 'r') as file:
        my_data = json.load(file)
    print("################################################")

    for image in my_data:
        min = -1
        for x in my_data[image]['color_pallet']:
            # dist = int(distance(color_to_find[0], color_to_find[1], color_to_find[2], x['color'][0], x['color'][1],
            #                     x['color'][2]) / (x['percentage'] / 10) * 1000) / 1000
            dist = int(distance(color_to_find[0], color_to_find[1], color_to_find[2], x['color'][0], x['color'][1],
                                x['color'][2]) * 1000) / 1000
            if min > dist or min == -1:
                min = dist
        my_data[image]['min_dist'] = min

    sorted_data = dict(sorted(my_data.items(), key=lambda x: x[1]['min_dist']))
    print(sorted_data)
    image_paths = []
    for image in sorted_data:
        print(image)
        image_paths.append(folder_path + '\\' + image)
    show_images(image_paths, color_to_find)

def go_trough(x, y):
    for i in range(x, y):

        image = pending_images[i]
        path = folder_path+'\\'+str(image)
        my_data[image] = {}
        print(i - x + 1, ' ', y-x+1)
        my_data[image]['color_pallet'] = get_pallete(path)

def thread():
    t1 = threading.Thread(target=go_trough, args=(first, length-1))
    # t2 = threading.Thread(target=go_trough, args=(second + 1, third))
    # t3 = threading.Thread(target=go_trough, args=(third + 1, forth))
    # t4 = threading.Thread(target=go_trough, args=(forth + 1, length - 1))

    t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

    t1.join()
    # t2.join()
    # t3.join()
    # t4.join()


def change_color():
    clear_photos()
    # try:
    #     clear_frame(frame)
    # except:
    #     print("error from change color")
    #     print()
    colors = askcolor(title="Tkinter Color Chooser")
    print("Color to find " + str(colors[0]))
    main(colors[0])


#On Open

folder_path = 'D:\images' #here choose the path to the folder with images
window = tk.Tk()
window.geometry('1000x500')
b1 = tk.Button(window,text='Select a Color',command=change_color)
b1.place(x = 0, y = 100)
b1.pack(expand=True)
pending_images = []


with open('data.json', 'r') as file:
    my_data = json.load(file)
print(my_data)
for image in os.listdir(folder_path):
    if str(image) in my_data:
        continue
    else:
        print("image is not here : ",end='')
        path = folder_path+'\\'+str(image)
        pending_images.append(image)
        # my_data[image] = {}
        # print(image)
        # my_data[image]['color_pallet'] = get_pallete(path)
print(len(pending_images) , " IMAGES TO ADD")
# 4 threads
#1  -> len / 4
length = len(pending_images)
first = 0
second = length // 4
third = length // 2
forth =3 * (length // 4)




thread()


write(my_data)
end_time = time.time()
print(end_time-start_time)
window.mainloop()


