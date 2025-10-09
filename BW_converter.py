from PIL import Image
import numpy as np
from skimage import color
from skimage.filters import laplace
from skimage.measure import shannon_entropy
from scipy.ndimage import generic_filter
from skimage.filters import rank
from skimage.morphology import disk
from skimage import exposure
from skimage.filters.rank import entropy

def convert_bw(image):
    bw_image = image.copy().convert('1', dither=Image.NONE)
    return bw_image

def convert_grey(bw_image):
    #bw_image_l = bw_image.convert('L')
    return bw_image

def convert_lv(bw_image):
    bw_image_l = bw_image.convert('L')
    image_np = np.array(bw_image_l).astype(np.float32) / 255.0

    laplacian_img = laplace(image_np, ksize=3)

    laplacian_abs = np.abs(laplacian_img)
    lap_norm = (laplacian_abs - laplacian_abs.min()) / (np.ptp(laplacian_abs) + 1e-5)
    lap_uint8 = (lap_norm * 255).astype(np.uint8)
    lv_image = Image.fromarray(lap_uint8, mode='L')

    return lv_image

def convert_lsd(image):
    bw_image_l = image.convert('L')
    gray_array = np.array(bw_image_l)
    gray_array = gray_array.astype(np.uint8)
    local_mean = rank.mean(gray_array, disk(1)).astype(np.float32)
    local_mean_sq = rank.mean(gray_array ** 2, disk(1)).astype(np.float32)
    diff = local_mean_sq - (local_mean ** 2)
    diff = np.clip(diff, 0, None)  # clip negative values to zero
    lsd_array = np.sqrt(diff)
    lsd_scaled = exposure.rescale_intensity(lsd_array, out_range=(0, 255)).astype(np.uint8)
    lsd_image = Image.fromarray(lsd_scaled)
    print(f"diff min: {diff.min()}, max: {diff.max()}")
    print(f"lsd_array min: {lsd_array.min()}, max: {lsd_array.max()}")
    #currently useless, maybe if we smooth the pixels first with a gausian blur
    return lsd_image

def convert_entropy(bw_image):
    bw_image_l = bw_image.convert('L')
    gray_array = np.array(bw_image_l).astype(np.uint8)
    entropy_img = entropy(gray_array, disk(3))
    entropy_scaled = exposure.rescale_intensity(entropy_img, out_range=(0, 255)).astype(np.uint8)
    entropy_image = Image.fromarray(entropy_scaled)
    return  entropy_image