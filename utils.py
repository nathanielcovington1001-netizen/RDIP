#!/usr/bin/env python3

from skimage import io, color
import numpy as np
from PIL import Image
from datetime import datetime
#!/usr/bin/env python3
import os

def create_folder():
    base_dir = "/home/rdipcod/RDIP2025/RDIP/images"
    os.makedirs(base_dir,exist_ok=True)
    existing_folders = [
        name for name in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, name)) and name.startswith("folder_")
    ]
    next_number = len(existing_folders)+ 1
    folder_name = f"img_{next_number:03d}"
    folder_path = os.path.join(base_dir,folder_name)
    os.makedirs(folder_path)
    print(f"created folder: {folder_path}")
    

def Create_pil_img(image_path):
    img = Image.open(image_path)
    return img

def create_array(img):
    img_array = np.array(img)
    return img_array
#output the array for use in other commands

def convert_bw(img, output_path):
    bw_img = img.copy().convert('1', dither=Image.NONE)
    return bw_img

def convert_lv(img_array, output_path):
    print("Running blob detection...")

def blob_detector1(img, output_path):
    print("Running blob detection...")
    
def blob_detector2(img_array, output_path):
    print("Running blob detection...")
    
#to do folder creator, blob detector, save info alongside images

#logic, create folder-> return folder directory-> give directory for the images -> return new image directory -> send directory to labels
