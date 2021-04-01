import os
import cv2 as cv
import glob

INPUT_FOLDER = 'data/abstract_1024/*'
OUTPUT_FOLDER = 'data/abstract_1024_modified/'
TARGET_SIZE = 1024
STEP_SIZE = 512

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
        # if i < 2:
        # im = cv.flip(im, 0)  # flip horizontally
        # cv.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
        # image_count += 1
        # im = cv.flip(im, 0)  # flip back
        # im = cv.flip(im, 1)
        # cv.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', im)
        # image_count += 1
        # im = cv.flip(im, 1)  # flip back
        im = cv.rotate(im, cv.cv2.ROTATE_90_CLOCKWISE)  # rotate


for image in images:
    im = cv.imread(image)

    # need to see if we need to crop or expand the image
    if im.shape[0] >= TARGET_SIZE and im.shape[1] >= TARGET_SIZE:
        print(f'Image name: {image}')

        # cropping the image in patches
        y = 0
        while y + TARGET_SIZE <= im.shape[0]:
            x = 0
            while x + TARGET_SIZE <= im.shape[1]:
                im_temp = im[y:y + TARGET_SIZE, x:x + TARGET_SIZE]
                rotate_and_save(im_temp)
                x += STEP_SIZE
            y += STEP_SIZE
    else:
        print(f'Image skiped: {image}')
