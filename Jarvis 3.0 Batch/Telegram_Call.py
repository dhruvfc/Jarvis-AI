import subprocess
from pyautogui import click
from keyboard import write
from time import sleep

def callal(name):
    subprocess.call(
        ["/usr/bin/open", "/Applications/Telegram.app"]
    )

    sleep(7)

    click(x=153, y=77)

    sleep(1)

    write(name)

    sleep(1)

    click(x=112, y=148)

    sleep(1)

    click(x=1294, y=80)

    sleep(1)