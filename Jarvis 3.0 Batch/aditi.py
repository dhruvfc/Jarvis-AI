import subprocess
from pyautogui import click
from keyboard import write
from keyboard import press
from time import sleep

def Whatsapp(name, message):

        subprocess.call(
            ["/usr/bin/open", "/Applications/WhatsApp.app"]
        )

        sleep(5)

        click(x=210, y=110)

        sleep(2)

        write(name)

        sleep(2)

        click(x=138, y=240)

        sleep(2)

        click(x=666, y=780)

        sleep(2)

        write(message)

        press('return')
