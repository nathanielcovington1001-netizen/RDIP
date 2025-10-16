#!/usr/bin/env/ python3

from skimage import io, color
import numpy as np
from PIL import image
from datetime import datetime

def Create_pil_img(image_path)
    img = Image.open(image_path)
    return = img

def create_array(img)
    img_array = np.array(img)
    return = img_array
#output the array for use in other commands

def convert_bw(img, output_path)
    bw_img = img.copy().convert('1', dither=Image.NONE)
    return = bw_img

def convert_lv(img_array, output_path)

def blob_detector1(img, output_path)
#detect blobs on bw_img
#name"previousname_blob"
# save to timestamped folder at output path
#return new image

def blob_detector2(img_array, output_path)
#detect blobs on unmodified image

#to do folder creator, blob detector, save info alongside images
