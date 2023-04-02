import selenium

import utils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"user-data-dir=C:/Users/gamet/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument(r'--profile-directory=Profile 1')

chrome_options.add_argument("headless")
browser = webdriver.Chrome(options=chrome_options)

browser.get("http://www.dmm.com/netgame/social/-/gadgets/=/app_id=854854/")


def main():
    test = utils.BrowserAction(browser)
    time.sleep(5)
    try:
        iframe1 = browser.find_element(By.TAG_NAME, "iframe")
        browser.switch_to.frame(iframe1)
    except NoSuchElementException:
        pass
    time.sleep(90)
    im = test.getClippedImage()
    imMatch = utils.ImageMatcher()
    imMatch.TemplateMatcher(img=im, template="assets/Image/util/login.png", browser=browser)
    while True:
        im = test.getClippedImage()
        imMatch = utils.ImageMatcher()
        imMatch.TemplateMatcher(img=im, template="assets/Image/util/login.png", browser=browser)
        time.sleep(5)


if __name__ == '__main__':
    main()
