from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.request
import time
import os

driver = webdriver.Chrome()
driver.get("https://www.beeple-crap.com/everydays")
wait = WebDriverWait(driver, 10)

# waits for the page to load
rounds = driver.find_elements_by_class_name('bDfMI')
print(len(rounds))

r = rounds[0]
r.click()

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
time.sleep(SCROLL_PAUSE_TIME)
while True:
    # Scroll down to bottom
    print('scrolling')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
# scroll back to the top
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)


# get all the images we can see
container = driver.find_element_by_id("pro-gallery-margin-container")
images = container.find_elements_by_tag_name("source")
print(len(images))
image = images[0]
if image.get_attribute("type") == 'image/jpg':
    print('true')
get_images(images)
# try to scrol down and see if that makes a difference
# look at any new images
# if we don't move scrolling down then exit

# clicks on the images
for image in images:
    image.click()
    # waits for the full screen image to load
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fullscreen-content')))
    # gets the src and name then saves the image
    full_image = driver.find_element_by_class_name("fullscreen-content")
    image_name = full_image.get_attribute("alt")
    src = full_image.get_attribute("src")
    urllib.request.urlretrieve(src, "data/" + image_name + ".png")
