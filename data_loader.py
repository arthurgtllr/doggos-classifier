import os
import pandas as pd
import constants
from utils import create_dir, snake_case
from tqdm import tqdm
import shutil

create_dir(constants.RAW_DATA_PATH, remove_if_exists=True)


if constants.PYTORCH_STRUCTURE:
    classes = [snake_case(doggo_class) for doggo_class in list(set(constants.DOGGO_CLASSES.keys()))]
    for doggo_class in classes:
        create_dir(constants.RAW_DATA_PATH + '/' + doggo_class)

def check_equivalent(breed):
    if breed in constants.EQUIVALENT_BREEDS.keys():
        return constants.EQUIVALENT_BREEDS[breed]

def get_breeds_paths():
    udacity_breeds_paths = {}
    oxford_breeds_paths = {}
    stanford_breeds_paths = {}
    for folder_name in os.listdir(constants.UDACITY_RAW_DATA_PATH + '/train'):
        breed = snake_case(folder_name.split('.')[1])
        udacity_breed_paths_train = [(constants.UDACITY_RAW_DATA_PATH + '/train/' + folder_name + '/' + file_name) for file_name in os.listdir(constants.UDACITY_RAW_DATA_PATH + '/train/' + folder_name)]
        udacity_breed_paths_test = [(constants.UDACITY_RAW_DATA_PATH + '/test/' + folder_name + '/' +  file_name) for file_name in os.listdir(constants.UDACITY_RAW_DATA_PATH + '/test/' + folder_name)]
        udacity_breed_paths_valid = [(constants.UDACITY_RAW_DATA_PATH + '/valid/' + folder_name + '/' + file_name) for file_name in os.listdir(constants.UDACITY_RAW_DATA_PATH + '/valid/' + folder_name)]
        udacity_breeds_paths[breed] = udacity_breed_paths_train + udacity_breed_paths_test + udacity_breed_paths_valid
    for file_name in os.listdir(constants.OXFORD_RAW_DATA_PATH):
        breed = snake_case(('_').join(file_name.split('_')[:-1]))
        if breed not in oxford_breeds_paths:
            oxford_breeds_paths[breed] = []
        oxford_breeds_paths[breed] = oxford_breeds_paths[breed] + [constants.OXFORD_RAW_DATA_PATH + '/' + file_name]
    for folder_name in os.listdir(constants.STANFORD_RAW_DATA_PATH):
        breed = snake_case(('-').join(folder_name.split('-')[1:]))
        stanford_breeds_paths[breed] = [(constants.STANFORD_RAW_DATA_PATH + '/' + folder_name + '/' + file_name) for file_name in os.listdir(constants.STANFORD_RAW_DATA_PATH + '/' + folder_name)]

    return {
        'udacity' : udacity_breeds_paths, 
        'oxford' : oxford_breeds_paths, 
        'stanford' :stanford_breeds_paths
    }

print('Paths retrieved, processing breeds ...')

df_doggos = pd.DataFrame()

for doggo_class, breeds in constants.DOGGO_CLASSES.items():
    # Creating a folder for each doggo class
    # doggo_class_path = constants.RAW_DATA_PATH + '/' + snake_case(doggo_class)
    # create_dir(doggo_class_path)
    
    # Filling the folder with the doggos from the breeds associated to the class
    df_doggos_class = pd.DataFrame()

    for dataset, breeds_paths in get_breeds_paths().items():
        for breed in breeds:
            breed_snake = snake_case(breed)
            if breed_snake in breeds_paths.keys():
                df_temp = pd.DataFrame(breeds_paths[breed_snake], columns=['file_path'])
                df_temp['dataset'] = dataset

                # Dealing with equivalent breeds
                equivalent_breed = check_equivalent(breed)
                if equivalent_breed:
                    print('Replacing ' + breed + ' by ' + equivalent_breed)
                    breed_snake = snake_case(equivalent_breed)
                
                df_temp['breed'] = breed_snake
                df_temp['class'] = snake_case(doggo_class)

                df_doggos_class = pd.concat([df_doggos_class, df_temp], ignore_index=True)

    df_doggos = pd.concat([df_doggos, df_doggos_class])

print('Moving the files ...')
for index, row in tqdm(df_doggos.iterrows()):
    src_dir = row['file_path']
    dst_name = ('-').join([row['class'], row['dataset'], str(index)]) + '.jpg'
    if constants.PYTORCH_STRUCTURE:
        dst_dir = constants.RAW_DATA_PATH + '/' + row['class'] + '/' + dst_name
    else:
        dst_dir = constants.RAW_DATA_PATH + '/' + dst_name
    row['new_file_path'] = dst_dir
    shutil.copy(src_dir,dst_dir)
    
df_doggos.to_csv(constants.DATA_PATH + '/raw_data.csv', index = False)



    

        
