## -*- coding: utf-8 -*-
#"""
#Created on Thu Jun  6 12:32:01 2019
#
#@author: bmusammartanov
import os
import imageio

def main():
    """
    Thi is the main program
    """
    location = os.getcwd()
    images = []
    try:
        filenames = sorted((fn for fn in os.listdir(location) if fn.endswith('.jpg'))) # this iteration technique has no built in order, so sort the frames
        for filename in filenames:
            images.append(imageio.imread(filename))
        #or the faster way images = list(map(lambda filename: imageio.imread(filename), filenames))
        imageio.mimsave(os.path.join('movie.gif'), images, duration=0.25, loop=0) # modify duration as needed
    except Exception as e:
        raise e
        print("No image files in here!")

if __name__ == "__main__":
    main()

