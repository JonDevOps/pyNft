##taken from Create Your Own NFT Collection With Python https://betterprogramming.pub/create-your-own-nft-collection-with-python-82af40abf99f
#0 Import the necessary packages
from PIL import Image
from IPython.display import display
import random
import json
import os

#1 Assign Trait Rarity
# Each image is made up of a series of traits
# The weightings for each trait drive the rarity and add up to 100%

face = ["White", "Black"]
face_weights = [60, 40]

ears = ["ears1", "ears2", "ears3", "ears4"]
ears_weights = [25, 30, 40, 1]

hair = ['hair1', 'hair10', 'hair11', 'hair12', 'hair2', 'hair3', 'hair4',
 'hair5',
 'hair6',
 'hair8',
 'hair9']
hair_weights = [10 , 10 , 10 , 10 ,10, 10, 10 ,10 ,10, 7 , 1 , 2]

mouth = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
mouth_weights = [10, 10, 50, 10,15, 5]

nose = ['n1', 'n2']
nose_weights = [90, 10]

#2 Classify your traits
# Dictionary variable for each trait.
# Each trait corresponds to its file name

face_files = {
    "white": "face1",
    "Black": "face2"
}

ears_files = {
    "ears1": "ears1",
    "ears2": "ears2",
    "ears3": "ears3",
    "ears4": "ears4"
}

eyes_files = {
    "regular": "eyes1",
    "small": "eyes2",
    "rayban": "eyes3",
    "hipster": "ears4"
}

hair_files = {
    "hair1": "hair1",
    "hair2": "hair2",
    "hair3": "hair3",
    "hair4": "hair4",
    "hair5": "hair5",
    "hair6": "hair6",
    "hair7": "hair7",
    "hair8": "hair8",
    "hair9": "hair9",
    "hair10": "hair10",
    "hair11": "hair11",
    "hair12": "hair12",
}

mouth_files = {
    "m1": "m1",
    "m2": "m2",
    "m3": "m3",
    "m4": "m4",
    "m5": "m5",
    "m6": "m6"
}

nose_files = {
    "n1": "n1",
    "n2": "n2"
}

#3 Define the images traits
## Generate Traits

TOTAL_IMAGES = 100 # Number of random unique images we want to generate

all_images = []

# A recursive function to generate unique image combinations
def create_new_image():

    new_image = {} #

    # For each trait catefgory, select a random trait based on the weighting
    new_image ["Face"] = random.choices(face, face_weights)[0]
    new_image ["Ears"] = random.choices(ears, ears_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]

    if new_image in all_images:
        return create_new_images()
    else:
        return new_image



# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)


##4 Validate uniqueness
#Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

os.mkdir(f'./images')

for item in all_images:

    im1 = Image.open(f'./scripts/face_parts/face/{face_files[item["Face"]]}.png').convert('RGBA')
    im2 = Image.open(f'./scripts/face_parts/eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./scripts/face_parts/ears/{ears_files[item["Ears"]]}.png').convert('RGBA')
    im4 = Image.open(f'./scripts/face_parts/hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im5 = Image.open(f'./scripts/face_parts/mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./scripts/face_parts/nose/{nose_files[item["Nose"]]}.png').convert('RGBA')      
    
    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)

    #Convert to RGB
    rgb_im = com5.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)