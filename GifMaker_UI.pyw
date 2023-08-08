# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com

Next is to open a avi to build a gif
https://www.freecodecamp.org/news/how-to-convert-video-files-to-gif-in-python/

"""
###Libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import os
import imageio

##Tkinter Window
root = tk.Tk()
root.geometry("300x220+300+300")
root.title("GIF MAKER")
root.resizable(width=False, height=False)


#Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
f_Ref = font.Font(family='Helvetica', size=12, weight='normal', underline=1)
font.families()

# main Frames
top_frame = tk.Frame(root, width=50)
top_frame.grid(row=0, column=0, rowspan=2, sticky="w")
top_frame.config(bg = '#AEBEDC')

######subframes
#Subframes - "Fluid Parameters"
frame00 = tk.LabelFrame(top_frame,text="Figures",width=500,height=150,font=f_H12B) 
frame00.grid(row=0, column=0, padx=8, ipady=5) #,padx=15,pady=10,ipadx=20,ipady=5
frame00.config(borderwidth=4, bg = '#AEBEDC')

frame_N = tk.LabelFrame(top_frame, width=40, height=25, text="Make GIF",font=f_H12B)
frame_N.grid(row=1, column=0, padx=8, ipady=5) #,pady=10,ipady=8, padx = 5 , ipadx = 20
frame_N.config(borderwidth=2, bg = '#AEBEDC')
##########################################

##Functions
def ex():
    """
    This destroys the UI
    """
    root.destroy()

def folder():
    """
    This function finds the folder
    """
    global location
    location = filedialog.askdirectory()
    
   
def name():
    """
    This function estimate the frost in evaporator
    """
    var = []
    var = [v0.get(), "."+ value_inside.get()]
    print(var)
    images = []
    filenames = sorted((fn for fn in os.listdir(location) if (fn.startswith(var[0]) and fn.endswith(var[1]) ))) # this iteration technique has no built in order, so sort the frames
    for filename in filenames: images.append(imageio.v2.imread(filename))
    imageio.mimsave(os.path.join(var[0]+'_.gif'), images, duration=0.1, loop=0) # modify duration as needed

###end of Functions

###########Main
#Text
text = ["Name prefix", "Figure extension"]

t1 = tk.Label(frame00,text=text[0], font=f_H12, bg = '#AEBEDC').grid(row=1,column=0,padx=10,pady=5)
v0 =  tk.StringVar()
t1 = tk.Entry(frame00, textvariable = v0 , width=14, justify="center",font=f_H12)
t1.grid(row = 1, column=1, padx=5, pady=5)
t1.insert("end",  "_")

#extension selection
extension_list = ["jpg", "jpeg", "png", "tiff"]
t2 = tk.Label(frame00,text=text[1], font=f_H12, bg = '#AEBEDC').grid(row=2,column=0,padx=10,pady=5,sticky='W')
value_inside = tk.StringVar(frame00)
question_menu = tk.OptionMenu(frame00, value_inside, *extension_list)
question_menu.grid(row = 2, column=1, padx=5, pady=5)
question_menu.config(font=f_H12, width=8, bg='#FFFFFF')
value_inside.set("jpeg")

t3 = tk.Button(frame00,text="Set the Figures Directory", font=f_H12, bg = '#AEBEDC',command=folder)
t3.grid(row=0,column=0,columnspan=2)
##########


##############Buttons
#Run button
run_butt = tk.Button(frame_N, text="GIF", font=f_H12, command = name)
run_butt.config(height=1, width=10)
run_butt.pack(side='left', fill='x', ipadx=2, padx=3, pady=5)

#Exit Button
ex = tk.Button(frame_N, text="EXIT", command=ex, font=f_H12)
ex.config(height=1, width=10)
ex.pack(side='right', fill='x', ipadx=2, padx=3, pady=5)


##########################
if __name__ == "__main__":
    root.mainloop()




