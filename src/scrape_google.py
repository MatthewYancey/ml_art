from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import urllib.request
import os
import glob
import time
import ssl

# urls
# images search: https://www.google.com/search?q=art&tbm=isch&hl=en&tbs=isz:l%2Csimg:CAESmwEJR7Ne5VG4PMQajwELELCMpwgaOwo5CAQSFPYb4yWVOaUx3gfiMd8l3xvFDrMZGhs7pf7iOjEn1wvHyixFEWDc_1vPkSDufLKhH2jMgBTAEDAsQjq7-CBoKCggIARIEnzny5gwLEJ3twQkaLwoUCgNhcnTapYj2AwkKBy9tLzBqancKFwoFcGFwZXLapYj2AwoKCC9tLzA2NDFrDA&sa=X&ved=0CAEQpwVqFwoTCJCQrdOSsO8CFQAAAAAdAAAAABAD&biw=1920&bih=976
# grey watercolor: https://www.google.com/search?q=grey%20abstract%20watercolor&tbm=isch&tbs=isz:l&hl=en-US&sa=X&ved=0CAEQpwVqFwoTCKjD7fbYr-8CFQAAAAAdAAAAABAL&biw=1200&bih=888
# white: https://www.google.com/search?q=white%20watercolor%20background&tbm=isch&hl=en&tbs=isz:l&sa=X&ved=0CAEQpwVqFwoTCOiIxpGVsO8CFQAAAAAdAAAAABAC&biw=1200&bih=888
# black and white: https://www.google.com/search?q=black%20and%20white%20paint%20abstract%20background&tbm=isch&hl=en&tbs=isz:l&sa=X&ved=0CAEQpwVqFwoTCMCGm-ebsO8CFQAAAAAdAAAAABAF&biw=1920&bih=976

url = 'https://www.google.com/search?q=black%20and%20white%20paint%20abstract%20background&tbm=isch&hl=en&tbs=isz:l&sa=X&ved=0CAEQpwVqFwoTCMCGm-ebsO8CFQAAAAAdAAAAABAF&biw=1920&bih=976'

ssl._create_default_https_context = ssl._create_unverified_context

# gets the image count
save_dir = os.getcwd() + '/data/images/'
current_images = glob.glob(save_dir + '*')
current_images = [int(os.path.basename(image).replace('.png', '')) for image in current_images]
if len(current_images) > 0:
    image_count = max(current_images) + 1
else:
    image_count = 0
print(image_count)

# sets up the driver
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)

# finds the mages
container = driver.find_element_by_id('islrg')
images = container.find_elements_by_xpath("div/div")
print(len(images))

# loops and saves them
i = 0
while i < len(images):
    # skip relateds search
    if "Related searches" not in images[i].text:
        images[i].click()
        time.sleep(1)
        large_image = driver.find_elements_by_class_name('n3VNCb')
        try:
            src = large_image[1].get_attribute('src')
            try:
                urllib.request.urlretrieve(src, save_dir + str(image_count) + ".png")
                image_count += 1
            except urllib.error.HTTPError:
                print('bad http')
        except IndexError:
            print('no second image')

        time.sleep(1)

    i += 1

    # updates the images
    images = container.find_elements_by_xpath("div/div")
    print(len(images))
