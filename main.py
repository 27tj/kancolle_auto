from kancolle_leveling import *
from kancolle_expedition import *
import State
import asyncio
import keyboard


async def main():
    await asyncio.wait_for(expedition(1, "02", 2), timeout=25)
    await asyncio.wait_for(expedition(5, "37", 3), timeout=25)
    await asyncio.wait_for(expedition(5, "38", 4), timeout=25)
    while True:
        try:
            if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl') and keyboard.is_pressed(
                    'shift') and keyboard.is_pressed('s'):
                print('Task ended by user')
                break
        except:
            continue
        while True:
            await asyncio.wait_for(leveling5_2_C(), timeout=90)
            if True in State.expStateFinish or searchImage("assets/expFinish.png")[0] != -1:
                break
            sleep(0.5)
        while searchImage("assets/expFinish.png")[0] != -1:
            clickImage("assets/expFinish.png")
            sleep(3)
            clickImage("assets/next.png")
            sleep(2)
            clickImage("assets/next.png")
            sleep(3)
        if State.expStateFinish[0]:
            State.expStateFinish[0] = False
            await asyncio.wait_for(expedition(1, "02", 2), timeout=25)
        if State.expStateFinish[1]:
            State.expStateFinish[1] = False
            await asyncio.wait_for(expedition(5, "37", 3), timeout=25)
        if State.expStateFinish[2]:
            State.expStateFinish[2] = False
            await asyncio.wait_for(expedition(5, "38", 4), timeout=25)


if __name__ == '__main__':
    asyncio.run(main())
