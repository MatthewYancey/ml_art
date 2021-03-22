import os
import cv2 as cv
import glob

INPUT_FOLDER = 'data/abstract_1024/*'
OUTPUT_FOLDER = 'data/abstract_1024_modified/'

# gets the list of images
images = glob.glob(INPUT_FOLDER)
print(f'Number of images: {len(images)}')

# function for ratating and saving each version of the images
image_count = 0


def rotate_and_save(im):
    global image_count
    for i in range(4):
        # first write
        cv.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
        image_count += 1
        if i < 2:
            im = cv.flip(im, 0)  # flip horizontally
            cv.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
            image_count += 1
            im = cv.flip(im, 0)  # flip back
            im = cv.flip(im, 1)
            cv.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
            image_count += 1
            im = cv.flip(im, 1)  # flip back
        im = cv.rotate(im, cv.cv2.ROTATE_90_CLOCKWISE)  # rotate


for image in images:
    im = cv.imread(image)
    print(f'Image name: {image}')
    rotate_and_save(im)
