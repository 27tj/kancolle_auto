from library import *
import asyncio
from time import *


async def leveling5_2_C():
    clickImage("assets/attack1.png")
    clickImage("assets/attack2.png")
    clickImage("assets/map5.png")
    clickImage("assets/5-2.png")
    clickImage("assets/confirm.png")
    sleep(1)
    if searchImage("assets/noResupply.png")[0] != -1:
        clickImage("assets/noResupply.png")
        clickImage("assets/resupply.png")
        clickImage("assets/resupply1.png")
        sleep(2)
        clickImage("assets/home.png")
        click([0, 0])
        clickImage("assets/attack1.png")
        clickImage("assets/attack2.png")
        clickImage("assets/map5.png")
        clickImage("assets/5-2.png")
        clickImage("assets/confirm.png")
    clickImage("assets/attack3.png")
    clickImage("assets/compass.png")
    clickImage("assets/next.png")
    clickImage("assets/next.png")
    clickImage("assets/retreat.png")


