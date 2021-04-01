from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.request
import os
import time


class get_art:

    def __init__(self):
        self.image_count = 0
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.beeple-crap.com/everydays")
        self.wait = WebDriverWait(self.driver, 10)

        # waits for the page to load
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bDfMI')))
        rounds = self.driver.find_elements_by_class_name('bDfMI')
        print(len(rounds))
        self.go_through_rounds(rounds)

    def scroll_to_bottom(self):
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            print('scrolling')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        # scroll back to the top
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    def go_through_rounds(self, rounds):
        # loops through the rounds
        for i in range(len(rounds)):
            rounds[i].click()
            print('new round')
            time.sleep(3)
            self.scroll_to_bottom()
            # wait for the images of that round to load
            # self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gallery-item-container')))
            # loop through the images
            self.get_images()

            # scroll back to the top
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(3)

    def get_images(self):
        container = self.driver.find_element_by_id("pro-gallery-margin-container")
        images = container.find_elements_by_tag_name("img")
        for image in images:
            self.save_image(image)

    def save_image(self, image):
        image_name = image.get_attribute("alt").replace('/', '')
        src = image.get_attribute("src")
        save_path = "data/" + str(self.image_count) + ".png"
        if os.path.exists(save_path):
            print('Image already captured')
        else:
            urllib.request.urlretrieve(src, save_path)
            self.image_count += 1


if __name__ == '__main__':
    get_art()
