from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.request
import time


class get_art:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.beeple-crap.com/everydays")
        self.wait = WebDriverWait(self.driver, 10)

        # waits for the page to load
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bDfMI')))
        rounds = self.driver.find_elements_by_class_name('bDfMI')
        print(len(rounds))
        self.go_through_rounds(rounds)

    def go_through_rounds(self, rounds):
        # loops through the rounds
        for i in range(len(rounds)):
            rounds[i].click()
            print('new round')
            # wait for the images of that round to load
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gallery-item-container')))
            # loop through the images
            time.sleep(5)
            self.get_images()

            # scroll back to the top
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(5)

    def get_images(self):
        images = self.driver.find_elements_by_class_name("gallery-item-container")
        print(len(images))
        i = 0
        while i < len(images):
            # gets the image to full screen and waits
            images[i].click()
            time.sleep(2)

            # gets the src and name then saves the image
            full_image = self.driver.find_element_by_class_name("fullscreen-content")
            image_name = full_image.get_attribute("alt")
            src = full_image.get_attribute("src")
            urllib.request.urlretrieve(src, "data/" + image_name + ".png")
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(2)

            # updates the image list
            images = self.driver.find_elements_by_class_name("gallery-item-container")
            print(len(images))
            i += 1


if __name__ == '__main__':
    get_art()
