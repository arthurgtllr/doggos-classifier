import pandas as pd
import constants
import random
import os
import glob
import cv2
import numpy as np
from tqdm import tqdm
import shutil

from utils import create_dir, center_crop

# Create the folder
create_dir(constants.PREPROCESSED_DATA_PATH, remove_if_exists=True)

if constants.PYTORCH_STRUCTURE:
    df_data = pd.read_csv(constants.RAW_DATA_PATH + '/raw_data.csv')
    classes = list(set(df_data['class'].values.tolist()))
    for doggo_class in classes:
        create_dir(constants.PREPROCESSED_DATA_PATH + '/' + doggo_class)

def preprocess_image(img, size = 212):
    # Resize
    img_resize = cv2.resize(img, (size,size), interpolation = cv2.INTER_AREA)

    return img_resize

def preprocess_image(img, size, padColor=255, keep_ratio=False, pytorch_structur=True, classes=[]):
    
    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    if keep_ratio:
        # aspect ratio of image
        aspect = w/h  

        # compute scaling and pad sizing
        if aspect > 1: # horizontal image
            new_w = sw
            new_h = np.round(new_w/aspect).astype(int)
            pad_vert = (sh-new_h)/2
            pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
            pad_left, pad_right = 0, 0
        elif aspect < 1: # vertical image
            new_h = sh
            new_w = np.round(new_h*aspect).astype(int)
            pad_horz = (sw-new_w)/2
            pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
            pad_top, pad_bot = 0, 0
        else: # square image
            new_h, new_w = sh, sw
            pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

        # set pad color
        if len(img.shape) is 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
            padColor = [padColor]*3

        # scale and pad
        scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
        scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)

    else:
        img_preprocessed = cv2.resize(img, (sh,sw), interpolation = interp)

    return img_preprocessed

for file_path in tqdm(glob.glob('{}/*.jpg'.format(constants.RAW_DATA_PATH))):
    file_name = file_path.split('/')[-1]
    img = cv2.imread(file_path)

    # Preprocessing
    img_preprocessed = preprocess_image(img=img, size=[212, 212], keep_ratio=False)

    if constants.PYTORCH_STRUCTURE:
        cv2.imwrite(constants.PREPROCESSED_DATA_PATH + '/' + file_name.split('-')[0] + '/' + file_name, img_preprocessed)
    else:
        cv2.imwrite(constants.PREPROCESSED_DATA_PATH + '/' + file_name, img_preprocessed)