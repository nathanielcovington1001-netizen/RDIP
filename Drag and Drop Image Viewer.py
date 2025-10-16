import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import BW_converter
import time
import shutil

def show_image(file_path, label):
    image = Image.open(file_path)
    image_copy = image.copy()
    image_copy.thumbnail((500, 500))
    img_tk = ImageTk.PhotoImage(image_copy)
    
    label.config(image=img_tk)
    label.image = img_tk

def save_img(file_path):

    BASE_SAVE_DIR = os.path.join(os.path.dirname(__file__), "Images")
    os.makedirs(BASE_SAVE_DIR, exist_ok=True)

    # Make unique folder name using filename + timestamp
    original_name = os.path.splitext(os.path.basename(file_path))[0]
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"{original_name}_{timestamp}"

    # Create full folder path under BASE_SAVE_DIR
    new_folder_path = os.path.join(BASE_SAVE_DIR, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Inside save_img, after creating new_folder_path
    original_copy_path = os.path.join(new_folder_path, os.path.basename(file_path))
    shutil.copy2(file_path, original_copy_path)

    return new_folder_path

def convert(file_path, folder_path):
    image = Image.open(file_path)

    bw_image = BW_converter.convert_bw(image)
    lv_image = BW_converter.convert_lv(bw_image)
    lsd_image = BW_converter.convert_lsd(image)
    entropy_image = BW_converter.convert_entropy(bw_image)

    # Save converted images and collect paths
    bw_path = os.path.join(folder_path, "converted_bw.png")
    lv_path = os.path.join(folder_path, "converted_lv.png")
    lsd_path = os.path.join(folder_path, "converted_lsd.png")
    entropy_path = os.path.join(folder_path, "converted_entropy.png")

    bw_image.save(bw_path)
    lv_image.save(lv_path)
    lsd_image.save(lsd_path)
    entropy_image.save(entropy_path)

    # Return paths so caller can use/display them
    return {
        "bw": bw_path,
        "lv": lv_path,
        "lsd": lsd_path,
        "entropy": entropy_path,
    }

def on_drop(event, label):
    file_path = event.data.strip('{}')
    show_image(file_path, label)
    new_folder = save_img(file_path)

    converted_paths = convert(file_path, new_folder)

    show_image(converted_paths["bw"], BW_img_label)
    show_image(converted_paths["lv"], LV_img_label)
    show_image(converted_paths["lsd"], LSD_img_label)
    show_image(converted_paths["entropy"], Entropy_img_label)

#GUI
# Create the main window
root = TkinterDnD.Tk()
root.title("Drag and Drop Image Viewer")
root.attributes('-zoomed', True)
root.configure(bg='#222222')  # Darker background

# Main container frame (fills the window)
main_frame = tk.Frame(root, bg='#222222')
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Left frame for original + BW images (larger)
left_frame = tk.Frame(main_frame, bg='#222222')
left_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 10))

# Right frame for LV, LSD, Entropy (smaller stacked)
right_frame = tk.Frame(main_frame, bg='#222222')
right_frame.grid(row=0, column=1, sticky='nsew')

# Make columns expandable proportionally
main_frame.columnconfigure(0, weight=2)  # Left bigger
main_frame.columnconfigure(1, weight=1)  # Right smaller
main_frame.rowconfigure(0, weight=1)

# --- LEFT SIDE ---

# Original Image label and image display
original_label = tk.Label(left_frame, text="Original Image", bg='#444444', fg='white', font=('Arial', 14))
original_label.pack(fill='x', pady=(0,5))

original_img_label = tk.Label(left_frame, text="Drop an image file here", bg='#555555', fg='white', width=60, height=25)
original_img_label.pack(fill='both', expand=True)

# BW Image label and image display
bw_label = tk.Label(left_frame, text="B&W Image", bg='#444444', fg='white', font=('Arial', 14))
bw_label.pack(fill='x', pady=(10,5))

BW_img_label = tk.Label(left_frame, text="B&W Image will appear here", bg='#555555', fg='white', width=60, height=25)
BW_img_label.pack(fill='both', expand=True)

# --- RIGHT SIDE ---

# For LV Image
lv_label = tk.Label(right_frame, text="LV Image", bg='#444444', fg='white', font=('Arial', 14))
lv_label.pack(fill='x', pady=(0,5))
LV_img_label = tk.Label(right_frame, text="LV Image will appear here", bg='#555555', fg='white', width=30, height=8)
LV_img_label.pack(fill='both', pady=(0,15), expand=True)

# For LSD Image
lsd_label = tk.Label(right_frame, text="LSD Image", bg='#444444', fg='white', font=('Arial', 14))
lsd_label.pack(fill='x', pady=(0,5))
LSD_img_label = tk.Label(right_frame, text="LSD Image will appear here", bg='#555555', fg='white', width=30, height=8)
LSD_img_label.pack(fill='both', pady=(0,15), expand=True)

# For Entropy Image
entropy_label = tk.Label(right_frame, text="Entropy Image", bg='#444444', fg='white', font=('Arial', 14))
entropy_label.pack(fill='x', pady=(0,5))
Entropy_img_label = tk.Label(right_frame, text="Entropy Image will appear here", bg='#555555', fg='white', width=30, height=8)
Entropy_img_label.pack(fill='both', expand=True)

# Register drop target on the original_img_label
original_img_label.drop_target_register(DND_FILES)
original_img_label.dnd_bind('<<Drop>>', lambda e: on_drop(e, original_img_label))

root.mainloop()
