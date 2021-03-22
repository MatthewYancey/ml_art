import os
import cv2
import glob

INPUT_FOLDER = 'data/output/*'
OUTPUT_FOLDER = 'data/output_frames/'

columns = 7
rows = 4
image_count = 0

images = glob.glob(INPUT_FOLDER)

for image in images:
    im = cv2.imread(image)
    width = im.shape[1]
    height = im.shape[0]
    step_x = width // columns
    step_y = height // rows

    x = 0
    y = 0
    while x + step_x <= width:
        y = 0
        while y + step_y <= height:
            temp_im = im[y:y + step_y, x:x + step_x]
            cv2.imwrite(f'{OUTPUT_FOLDER}{image_count}.png', temp_im)
            image_count += 1
            y += step_y
        x += step_x
