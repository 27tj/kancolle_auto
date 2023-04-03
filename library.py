import cv2
from python_imagesearch.imagesearch import imagesearch
from time import *
import random
import pyautogui


def searchImage(image):
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    pos = imagesearch(image)
    print(image, pos)
    if pos[0] != -1:
        x = (pos[0] + round(img.shape[1] / 2)) + random.randint(-2, 3)
        y = (pos[1] + round(img.shape[0] / 2)) + random.randint(-2, 3)
        return x, y
    else:
        return pos


def click(pos):
    x = pos[0]
    y = pos[1]
    if x != -1 and y != -1:
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.doubleClick()
        pyautogui.click()


def clickImage(image):
    sleep(1)
    n = 0
    pos = searchImage(image)
    while pos[0] == -1:
        pos = searchImage(image)
        n += 1
        if n == 10:
            break
        sleep(0.5)
    if pos[0] != -1 and pos[1] != -1:
        print(image, pos)
        click(pos)
