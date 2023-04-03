from kancolle_leveling import *
from kancolle_expedition import *
import State
import asyncio
import keyboard
import pyautogui


async def main():
    sleep(1)
    await asyncio.wait_for(expedition(1, "02", 2), timeout=25)
    await asyncio.wait_for(expedition(1, "04", 3), timeout=25)
    await asyncio.wait_for(expedition(1, "05", 4), timeout=25)
    while True:
        exp_end = False
        try:
            if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl') and keyboard.is_pressed(
                    'shift') and keyboard.is_pressed('s'):
                print('Task ended by user')
                break
        except:
            continue
        while True:
            n = 0
            await asyncio.wait_for(leveling5_2_C(), timeout=90)
            while n < 20:
                n += 1
                if (True in State.expStateFinish) or searchImage("assets/Image/expedition/expFinish.png")[0] != -1:
                    exp_end = True

                    sleep(0.05)
                    break
            if exp_end:
                break
            sleep(0.5)
        while searchImage("assets/Image/expedition/expFinish.png")[0] != -1:
            clickImage("assets/Image/expedition/expFinish.png")
            sleep(3)
            clickImage("assets/Image/util/next.png")
            sleep(2)
            clickImage("assets/Image/util/next.png")
            sleep(3)
        if State.expStateFinish[0] :
            State.expStateFinish[0] = False
            await asyncio.wait_for(expedition(1, "02", 2), timeout=25)
        if State.expStateFinish[1]:
            State.expStateFinish[1] = False
            await asyncio.wait_for(expedition(1, "04", 3), timeout=25)
        if State.expStateFinish[2]:
            State.expStateFinish[2] = False
            await asyncio.wait_for(expedition(1, "05", 4), timeout=25)


if __name__ == '__main__':
    asyncio.run(main())
