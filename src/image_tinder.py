import os
import shutil
import glob
import cv2

read_path = '/data/keep/*'
keep_path = '/data/keep/'

images = glob.glob(os.getcwd() + read_path)
print(len(images))
for image in images:
    im = cv2.imread(image)
    cv2.imshow('image', im)
    key = cv2.waitKey(0)

    if key == 3:
        shutil.move(image, os.getcwd() + '/data/keep_good/' + os.path.basename(image))
    if key == 2:
        shutil.move(image, os.getcwd() + '/data/keep_modify/' + os.path.basename(image))
