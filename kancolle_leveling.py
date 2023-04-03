from library import *
import asyncio
from time import *
import pyautogui

async def leveling5_2_C():
    clickImage("assets/Image/util/attack1.png")
    clickImage("assets/Image/util/attack2.png")
    clickImage("assets/Image/新增資料夾/map5.png")
    clickImage("assets/Image/新增資料夾/5-2.png")
    clickImage("assets/Image/util/confirm.png")
    sleep(2)
    if searchImage("assets/Image/util/noResupply.png")[0] != -1:
        clickImage("assets/Image/util/resupply.png")
        clickImage("assets/Image/util/resupply1.png")
        sleep(1)
        clickImage("assets/Image/util/home.png")
        pyautogui.moveTo(960, 540, duration=1.5)
        clickImage("assets/Image/util/attack1.png")
        clickImage("assets/Image/util/attack2.png")
        clickImage("assets/Image/新增資料夾/map5.png")
        clickImage("assets/Image/新增資料夾/5-2.png")
        clickImage("assets/Image/util/confirm.png")
    clickImage("assets/Image/util/attack3.png")
    clickImage("assets/Image/util/compass.png")
    sleep(40)
    clickImage("assets/Image/util/next.png")
    sleep(2)
    clickImage("assets/Image/util/next.png")
    sleep(1)
    clickImage("assets/Image/util/retreat.png")
    pyautogui.moveTo(960, 540, duration=1.5)
    sleep(1)

