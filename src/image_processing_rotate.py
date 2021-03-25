import os
import cv2
import glob

INPUT_FOLDER = 'data/arrival/*'
OUTPUT_FOLDER = 'data/arrival_1024_rotated/'

# gets the list of images
images = glob.glob(INPUT_FOLDER)
print(f'Number of images: {len(images)}')

# function for ratating and saving each version of the images
image_count = 0


def rotate_and_save(im):
    global image_count
    for i in range(4):
        # first write
        cv2.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
        image_count += 1
        if i < 2:
            im = cv2.flip(im, 0)  # flip horizontally
            cv2.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
            image_count += 1
            im = cv2.flip(im, 0)  # flip back
            im = cv2.flip(im, 1)
            cv2.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
            image_count += 1
            im = cv2.flip(im, 1)  # flip back
        im = cv2.rotate(im, cv2.cv2.ROTATE_90_CLOCKWISE)  # rotate


for image in images:
    im = cv2.imread(image)
    print(f'Image name: {image}')
    im = cv2.resize(im, (1024, 1024))
    rotate_and_save(im)
