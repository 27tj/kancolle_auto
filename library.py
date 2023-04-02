import cv2
import win32api
import win32con
from python_imagesearch.imagesearch import imagesearch
from time import *
import random


def searchImage(image):
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    pos = imagesearch(image)
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
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


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
        click(pos)
