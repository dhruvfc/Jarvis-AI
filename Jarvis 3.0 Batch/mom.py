import subprocess
from pyautogui import click
from keyboard import write
from keyboard import press
from time import sleep


def Whatsappvideomom(name):
    subprocess.call(
        ["/usr/bin/open", "/Applications/WhatsApp.app"]
    )

    sleep(7)

    click(x=152, y=109)

    sleep(1)

    write(name)

    sleep(1)

    click(x=166, y=243)

    sleep(1)

    click(x=1233, y=55)

    sleep(1)


