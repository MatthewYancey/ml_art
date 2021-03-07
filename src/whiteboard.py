from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.request
import time

driver = webdriver.Chrome()
driver.get("https://www.beeple-crap.com/everydays")
wait = WebDriverWait(driver, 10)

# waits for the page to load
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bDfMI')))
rounds = driver.find_elements_by_class_name('bDfMI')
# rounds = driver.find_elements_by_partial_link_text('ROUND')
# rounds = driver.find_element_by_id("comp-k5s8azvg__c14d874f-bcc3-41bf-bc15-ac9c43df9e99")
# rounds = rounds[20:]
print(len(rounds))
# rounds = driver.find_elements_by_class_name("bDfMI")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

r = rounds[5]
r.click()
driver.get("https://www.beeple-crap.com/everydays")
for r in rounds[5:]:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bDfMI')))
    r.click()
    print('new round')
    # wait for the images of that round to load
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gallery-item-container')))
    time.sleep(10)

# get all the images we can see
images = driver.find_elements_by_class_name("gallery-item-container")
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
