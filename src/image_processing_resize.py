import os
import cv2 as cv
import glob

INPUT_FOLDER = 'data/abstract/*'
OUTPUT_FOLDER = 'data/abstract_modified/'
TARGET_SIZE = 1024

# gets the list of images
images = glob.glob(INPUT_FOLDER)
print(f'Number of images: {len(images)}')

# function for resizing and saving each version of the images
image_count = 0

for image in images:
    print(image)
    im = cv.imread(image)
    im = cv.resize(im, (TARGET_SIZE, TARGET_SIZE))
    cv.imwrite(OUTPUT_FOLDER + str(image_count) + '.png', im)
    image_count += 1
