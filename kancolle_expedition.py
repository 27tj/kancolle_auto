import time

from library import *
import asyncio
import State
import time
import pyautogui

expTime = [15, 30, 20, 50, 90, 40, 60, 180, 240, 90, 300, 480, 240, 360, 720, 900, 45, 300, 360, 120, 140, 180, 240,
           500]


async def expedition(map_no, exp_no, team_no):
    print("hi")
    clickImage("assets/Image/util/attack1.png")
    clickImage("assets/Image/util/expedition.png")
    if map_no != 1:
        clickImage(f'assets/Image/expedition/expMap{map_no}.png')
    clickImage(f'assets/Image/expedition/expedition_no/exp{exp_no}.png')
    clickImage(f'assets/Image/util/confirm.png')
    sleep(0.5)
    if team_no != 2:
        clickImage(f'assets/Image/team/team{team_no}.png')
        sleep(0.2)
    pos = searchImage("assets/Image/expedition/expResupply.png")
    if pos[0] != -1:
        clickImage("assets/Image/expedition/expResupply.png")
        sleep(1.5)
    if searchImage("assets/Image/expedition/expStart.png") != -1:
        clickImage("assets/Image/expedition/expStart.png")
    elif searchImage("assets/Image/expedition/expStart2.png"):
        clickImage("assets/Image/expedition/expStart2.png")
    time.sleep(1.5)
    clickImage("assets/Image/util/home.png")

    pyautogui.moveTo(960, 540, duration=1.5)
    asyncio.create_task(wait_for_exp(exp_no, team_no))
    print("exp started")


async def wait_for_exp(exp_no, team_no):
    print(f"wait for exp {exp_no} end")
    await asyncio.sleep(expTime[int(exp_no) - 1]*60)
    State.expStateFinish[team_no - 2] = True
    print(State.expStateFinish)
