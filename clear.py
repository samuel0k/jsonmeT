import os
import platform


def clear():
    plat = platform.system()

    if plat == "Windows":
        os.system('cls')
    elif plat == "Linux":
        os.system('clear')