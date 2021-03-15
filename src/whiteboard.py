from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.request
import os
import glob
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# gets the image count
save_dir = os.getcwd() + '/data/images/'
current_images = glob.glob(save_dir + '*')
current_images = [int(os.path.basename(image).replace('.png', '')) for image in current_images]
image_count = max(current_images) + 1
print(image_count)

# sets up the driver
driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=grey+abstract+watercolor&tbm=isch&ved=2ahUKEwiis8OMzq_vAhUpgE4HHRNIA6kQ2-cCegQIABAA&oq=grey+abstract+watercolor&gs_lcp=CgNpbWcQAzIGCAAQCBAeMgYIABAIEB4yBggAEAgQHlDT-AFY0_gBYNH9AWgAcAB4AIABRYgBRZIBATGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=HepNYOKwH6mAuuoPk5CNyAo&bih=976&biw=1792")
wait = WebDriverWait(driver, 10)

# finds the mages
container = driver.find_element_by_id('islrg')
images = container.find_elements_by_xpath("div/div")

# loops and saves them
for image in images:
    image.click()
    time.sleep(1)
    large_image = driver.find_element_by_class_name('n3VNCb')
    src = large_image.get_attribute("src")
    urllib.request.urlretrieve(src, save_dir + str(image_count) + ".png")
    image_count += 1


