import os
import glob
from PIL import Image

resize_value = 256

images = glob.glob('data/210/*')
for image in images:
    print(image)
    im = Image.open(image)
    new_im = im.resize((resize_value, resize_value))
    new_im.save('data/' + str(resize_value) + '/' + os.path.basename(image))
