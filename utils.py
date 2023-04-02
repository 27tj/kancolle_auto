import cv2
from PIL import Image
from selenium import webdriver
from io import BytesIO
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BrowserAction(object):

    def __init__(self, browser):
        self.browser = browser

    def getClippedImage(self):
        screenshot = self.browser.get_screenshot_as_png()
        # Load the screenshot into PIL Image object
        screenshot_pil = Image.open(BytesIO(screenshot))

        # Convert the PIL Image object to OpenCV image
        screenshot_cv = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR, 0)
        return screenshot_cv

    def elementAction(self, x, y):
        actions = ActionChains(self.browser)
        actions.move_by_offset(x, y).click().perform()


class ImageMatcher(object):

    def __init__(self):
        self.locator = None
        self.y = None
        self.x = None
        self.template = None
        self.img = None
        self.height = None
        self.width = None
        self.threshold = None
        self.methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                        cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    @property
    def center_x(self):
        return self.x + int(self.width / 2) \
            if self.x and self.width else None

    @property
    def center_y(self):
        return self.y + int(self.height / 2) \
            if self.y and self.height else None

    def TemplateMatcher(self, img, template, browser):
        self.locator = img
        self.img = img
        self.template = cv2.imread(template)
        self.height = cv2.imread(template).shape[0]
        self.width = cv2.imread(template).shape[1]
        action = BrowserAction(browser)

        for method in self.methods:
            # img2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
            img2 = img.copy()
            result = cv2.matchTemplate(img2, cv2.imread(template), method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                location = min_loc
            else:
                location = max_loc
            self.x, self.y = location
            bottom_right = (location[0] + self.width, location[1] + self.height)
            print(location)
            print(bottom_right)
            cv2.rectangle(img2, location, bottom_right, 255, 5)
            while True:
                cv2.imshow('Match', img2)
                k = cv2.waitKey(0)
                if k == 121:
                    action.elementAction(x=location[0] + int(self.width / 2), y=location[1] + int(self.height / 2))
                    break
                elif k == 110:
                    cv2.destroyAllWindows()
                    break
