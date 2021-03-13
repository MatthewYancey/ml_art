import os
import glob
from PIL import Image

check_size = 210
check_channels = 3

images = glob.glob('data/210/*')
for image in images:
    # print(image)
    im = Image.open(image)
    # print(im.mode)
    if im.mode != 'RGB':
        print(image)
    # new_im = im.resize((resize_value, resize_value))
    # new_im.save('data/' + str(resize_value) + '/' + os.path.basename(image))
