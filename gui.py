#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageTk
import utils
import main
import os

#---
script_dir = os.path.dirname(os.path.abspath(__file__))
folder_num = 1
current_folder = "img_001"
image_folder = os.path.join("images",current_folder )
image_path1 = os.path.join(script_dir, image_folder, "blob_img_001.jpeg")
image_path2 = os.path.join(script_dir, image_folder, "blob_img_001.jpeg")
image_path3 = os.path.join(script_dir, image_folder, "blob_img_001.jpeg")

#---
def close_window():
	root.destroy()

def next_folder():
	global folder_num 
	folder_num = folder_num + 1
	load_images()
	print("next folder", folder_num)
	
def load_image(path, label):
    try:
        pil_img = Image.open(path)
        tk_img = ImageTk.PhotoImage(pil_img)
        label.config(image=tk_img, text=label.orig_text, compound=tk.TOP)
        label.image = tk_img
    except Exception as e:
        print(f"Error loading {path}: {e}")
        label.config(text="Image not found", image='', compound=tk.TOP)
        label.image = None
    
    
def load_images():
    global folder_num
    global pil_image1, pil_image2, pil_image3
    global tk_image1, tk_image2, tk_image3
    global image1, image2, image3
    
    current_folder = f"img_{folder_num:03d}"
    image_folder = os.path.join(script_dir, "images",current_folder )
    
    image_path1 = os.path.join(script_dir, image_folder, f"og_img_{folder_num:03d}.jpeg")
    image_path2 = os.path.join(script_dir, image_folder, f"bw_img_{folder_num:03d}.jpeg")
    image_path3 = os.path.join(script_dir, image_folder, f"blob_img_{folder_num:03d}.jpeg")
    
    load_image(image_path1,image1)
    load_image(image_path2,image2)
    load_image(image_path3,image3)
	

#----

root = tk.Tk()
root.geometry("300x300")
root.attributes('-fullscreen', True)

menu_bar = tk.Frame(root, bg="lightgray", height=40)
menu_bar.grid(row=0, column=0, sticky="ew")

root.grid_columnconfigure(0, weight=50)
root.grid_columnconfigure(1, weight=50)
root.grid_columnconfigure(2, weight=50)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=50)
root.grid_rowconfigure(2, weight=50)

#Button1 for closing window
button1 = tk.Button(menu_bar, text = "X", command = close_window)
button1.grid(row=0, column=3, padx=0, pady=0)

#button2
button2 = tk.Button(menu_bar, text = "Create folder", command = utils.create_folder)
button2.grid(row=1, column=2, sticky="ew", padx=10, pady=5)

#button3
button3 = tk.Button(menu_bar, text = "Capture Image", command = main.capture_image)
button3.grid(row=2, column=2, sticky="ew", padx=10, pady=5)

#button4
button4 = tk.Button(menu_bar, text = "Next Folder", command = next_folder)
button4.grid(row=3, column=2, sticky="ew", padx=10, pady=5)

#button5
button5 = tk.Button(menu_bar, text = "Previous Folder", command = previous_folder)
button5.grid(row=4, column=2, sticky="ew", padx=10, pady=5)

#image 1
pil_image1 = Image.open(image_path1)
tk_image1 = ImageTk.PhotoImage(pil_image1)
image1 = tk.Label(root, text="Original Image", image=tk_image1, compound=tk.TOP)
image1.orig_text = "Original Image"
image1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

#image 2
pil_image2 = Image.open(image_path2)
tk_image2 = ImageTk.PhotoImage(pil_image2)
image2 = tk.Label(root, text="BW Image", image=tk_image2, compound=tk.TOP)
image2.orig_text = "BW Image"
image2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

#image 3
pil_image3 = Image.open(image_path3)
tk_image3 = ImageTk.PhotoImage(pil_image3)
image3 = tk.Label(root, text="Blob detection", image=tk_image3, compound=tk.TOP)
image3.orig_text = "Blob detection"
image3.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

root.mainloop()
