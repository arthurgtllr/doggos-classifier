# Paths of the raw datasets

OXFORD_RAW_DATA_PATH = "./data/raw_data_all/oxford/images"
STANFORD_RAW_DATA_PATH = "./data/raw_data_all/stanford/images/Images"
UDACITY_RAW_DATA_PATH = "./data/raw_data_all/dogImages"

# Path to gathered data

DATA_PATH = './data'
RAW_DATA_PATH = './data/raw_data'
PREPROCESSED_DATA_PATH = './data/preprocessed_data'

# Whether the structure of data needs to follow pytorch needs, i.e. each file in a subfolder named after its class
PYTORCH_STRUCTURE = True

# Breed per class
DOGGO_CLASSES = {
    'Long Boi' : ['Italian Greyhound', 'Greyhound', 'Saluki', 'Borzoi', 'Ibizan Hound', 'Afghan Hound'],
    'Moon Moon' : ['Siberian Husky', 'Alaskan Malamute', 'Samoyed', 'Akita', 'Shiba Inu'],
    'Woofer' : ['Great Dane', 'Doberman', 'Doberman Pinscher', 'Beauceron', 'Greater Swiss Mountain Dog'],
    'Floofer' : ['Newfoundland', 'Leonberger', 'Leonberg', 'Chow', 'Chow Chow', 'Tibetan Mastiff', 'Bernese Mountain Dog'],
    'Hot Dog' : ['Dachshund', 'Basset', 'Basset Hound', 'Cardigan Welsh Corgi', 'Pembroke Welsh Corgi'],
    'Wrinkler' : ['French Bulldog', 'Chinese Shar-Pei', 'Pug', 'Neapolitan Mastiff', 'Dogue de Bordeaux'],
    'Best Boi' : ['Labrador Retriever', 'Golden Retriever', 'Cheseapeake Bay Retriever', 'Curly Coated Retriever', 'Nova Scotia Duck Tolling Retriever', 'Flat Coated Retriever']
}

EQUIVALENT_BREEDS = {
    'Chow' : 'Chow Chow',
    'Leonberg' : 'Leonberger',
    'Basset' : 'Basset Hound'
}