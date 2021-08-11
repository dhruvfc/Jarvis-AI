import subprocess
from pyautogui import click
from keyboard import write
from keyboard import press
from time import sleep

def chat(name, message):
    subprocess.call(
        ["/usr/bin/open", "/Applications/Telegram.app"]
    )

    sleep(7)

    click(x=138, y=75)

    sleep(1)

    write(name)

    sleep(0.5)

    click(x=162, y=136)

    sleep(0.5)

    click(x=703, y=790)

    sleep(0.5)

    write(message)

    press('return')