# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com

Next is to open a avi to build a gif
https://www.freecodecamp.org/news/how-to-convert-video-files-to-gif-in-python/

"""
import tkinter as tk
from tkinter import messagebox, filedialog, font
import os
from PIL import Image
from imageio import mimsave
import re
from moviepy.video.io.VideoFileClip import VideoFileClip
from threading import Thread

# Tkinter Window
root = tk.Tk()
root.geometry("455x219+300+300")
root.title("GIF MAKER")
root.resizable(width=False, height=False)

# Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
f_Ref = font.Font(family='Helvetica', size=12, weight='normal', underline=1)

# Main Frames
top_frame = tk.Frame(root, width=50)
top_frame.grid(row=0, column=0, rowspan=2, sticky="w")
top_frame.config(bg='#AEBEDC')

# Subframes
frame00 = tk.LabelFrame(top_frame, text="From Figures", width=250, height=150, font=f_H12B)
frame00.grid(row=0, column=0, padx=8, ipady=5)
frame00.config(borderwidth=2, bg='#AEBEDC')

frame01 = tk.LabelFrame(top_frame, text="From Video", width=200, height=150, font=f_H12B)
frame01.grid(row=0, column=1, padx=8, ipady=5)
frame01.config(borderwidth=2, bg='#AEBEDC')

# Variables
location = ""

# Functions
def ex():
    root.destroy()

def folder():
    global location
    location = filedialog.askdirectory()

def extract_numeric_part(filename):
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group())
    return -1

def video():
    video_name = filedialog.askopenfile(initialdir="/", title="Select Video File",
                                           filetypes=(("avi", "*.avi"), ("mp4", "*.mp4")))
    vname = str(video_name.name)
    videoClip = VideoFileClip(vname)
    
    f_name_ext = os.path.basename(vname)
    f_name = os.path.splitext(f_name_ext)[1]+ ".gif"
    videoClip.write_gif(f_name,program="ffmpeg")
   
    videoClip.close()
    messagebox.showinfo("GIF Created", f"The GIF {f_name} is saved")
   

def create_gif():
    prefix = prefix_entry.get()
    extension = extension_dropdown.get()
    duration = float(duration_entry.get())
    
    if not location:
        messagebox.showerror("Error", "Please select a folder.")
        return
    
    images = []
    files = os.listdir(location)
    file_filtered = [file for file in files if file.startswith(prefix) and file.endswith(extension)]
    file_filtered.sort(key=extract_numeric_part)
    
    if not file_filtered:
        messagebox.showerror("Error", "No matching images found.")
        return
    
    try:
        # Open all images to get the size of the first image
        first_image = Image.open(os.path.join(location, file_filtered[0]))
        first_image_size = first_image.size
        images.append(first_image)

        for file_name in file_filtered[1:]:
            file_path = os.path.join(location, file_name)
            img = Image.open(file_path)
            # Resize image to match the first image size if different
            if img.size != first_image_size:
                img = img.resize(first_image_size, Image.ANTIALIAS)
            images.append(img)
        
        output = f"{prefix}_.gif"
        gif_path = os.path.join(location, output)
        mimsave(gif_path, images, duration=duration, loop=0)
        messagebox.showinfo("GIF Created", f"The GIF {output} is saved here:\n{location}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        
##Threads
def threading_0():
    #call function video()
    t0 = Thread(target=video)
    t0.start()
##Threads
def threading_1():
    #call function create_gif()
    t1 = Thread(target=create_gif)
    t1.start()
    
# UI Elements
t1 = tk.Label(frame00, text="Name prefix", font=f_H12, bg='#AEBEDC')
t1.grid(row=1, column=0, padx=10, pady=5)
prefix_entry = tk.Entry(frame00, width=14, justify="center", font=f_H12)
prefix_entry.grid(row=1, column=1, padx=5, pady=5)
prefix_entry.insert("end", "_")

text2 = tk.Label(frame00, text="Figure extension", font=f_H12, bg='#AEBEDC')
text2.grid(row=2, column=0, padx=10, pady=5, sticky='W')
extension_list = ["jpg", "jpeg", "png", "tiff"]
extension_dropdown = tk.StringVar(frame00)
question_menu = tk.OptionMenu(frame00, extension_dropdown, *extension_list)
question_menu.grid(row=2, column=1, padx=5, pady=5)
question_menu.config(font=f_H12, width=8, bg='#FFFFFF')
extension_dropdown.set("jpeg")

t1_2 = tk.Label(frame00, text="Duration sec/frame", font=f_H12, bg='#AEBEDC')
t1_2.grid(row=3, column=0, padx=10, pady=5)
duration_entry = tk.Entry(frame00, width=14, justify="center", font=f_H12)
duration_entry.grid(row=3, column=1, padx=5, pady=5)
duration_entry.insert("end", "1")

t3 = tk.Button(frame00, text="Set the Figures Directory", font=f_H12, command=folder)
t3.grid(row=0, column=0, columnspan=2)

#Video Buttons
video_btn = tk.Button(frame01, text="Select a Video\n&\nConvert to GIF",
                        command = threading_0, font=f_H12, bg='#FFFFFF')
video_btn.pack(expand=True)

run_button = tk.Button(frame00, text="GIF from Figures", font=f_H12, command=threading_1)
run_button.config(height=1)
run_button.grid(row=4, column=0, columnspan = 2, padx=5, pady=5)

##exit_button = tk.Button(frame_N, text="EXIT", command=ex, font=f_H12)
##exit_button.pack(fill='x', ipadx=2, padx=3, pady=5)
##
if __name__ == "__main__":
    root.mainloop()
