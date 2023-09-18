# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com

"""
# importing os module
import os
import tkinter as tk
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.geometry("301x218+300+300")
root.title("RenameFiles")
root.resizable(width=False, height=True)

location = askdirectory(title='Select Folder') # shows dialog box and return the path

# Function to rename multiple files
def main():
    filenames = sorted( (fn for fn in os.listdir(location) if (fn.endswith(".jpg") )) )# this iteration technique has no built in order, so sort the frames
    filenames =[(location + "\\" +  fn) for fn in filenames]
    for count, filename in enumerate(filenames):
        suffix = "Vel_"
        #time = str(5500+(count*500))
        time = str(count)
        ext = ".jpg"
        #ext = ".dat.h5"
        new_name = suffix + time + ext
        print(new_name)
        os.rename(filename, new_name)
        tk.Label(root, text = new_name).pack()

# Define a function to close the window
def close():
   root.destroy()
   
# Driver Code
if __name__ == '__main__': 
    # Calling main() function
    main()
    tk.Button(root, text = "Exit", command = close).pack()
    root.mainloop()
