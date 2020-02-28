import os
import re
import shutil

def create_dir(path, remove_if_exists=False):
    if remove_if_exists:
        try:
            shutil.rmtree(path)
        except OSError as e:
            print ("Removal of the directory %s failed" % path)
            print(e)
    else:
        print ("Successfully created the directory %s " % path)

    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as e:
            print ("Creation of the directory %s failed" % path)
            print(e)
        else:
            print ("Successfully created the directory %s " % path)


def snake_case(string):
    string_no_space = re.sub(' ', '_', string)
    string_dash = re.sub('-', '_', string_no_space)
    return string_dash.lower()

def random_crop(list_of_np_arrays):
    cropped = []
    for np_array in list_of_np_arrays:
        w, h = np_array.shape[1], np_array.shape[0]
        img = array_to_img(np_array, scale=False)
        top = random.randint(0,h-224)
        bottom = top + 224
        left = random.randint(0,w-224)
        right = left + 224
        img = img.crop((left, top, right, bottom))
        cropped.append(img_to_array(img))
    return np.array(cropped)

def center_crop(list_of_np_arrays):
    cropped = []
    for np_array in list_of_np_arrays:
        w, h = np_array.shape[1], np_array.shape[0]
        img = array_to_img(np_array, scale=False)
        img = img.crop((w/2  - 112, h/2 - 112, w/2 + 112, h/2 + 112))
        cropped.append(img_to_array(img))
    return np.array(cropped)

def scale_pixels(list_of_np_arrays):
    scaled_arrays = []
    for np_array in list_of_np_arrays:
        scaled_arrays.append(np_array / 255)
    return np.array(scaled_arrays)
