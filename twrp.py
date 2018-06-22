#!/usr/bin/python3
import os
import sys
import time
from colorama import Fore, Back, Style, init

init()

def twrpInstaller(device,platform):
    if platform == "l":
        platform = "Linux"
        clear = lambda: os.system('clear')
    elif platform == "w":
        platform = "Windows"
        clear = lambda: os.system('cls')
    print ("Ok, to be sure your device is " + device + " and, you are using "+ platform +" os")
    print ("Ok, so lets beggin")
    print ("First, simply drag and drop your *.img file on this window :")
    pathToTwrp = input()
    clear()
    print ("And now, let's the magic beggin")
    os.system("adb reboot bootloader")
    os.system("fastboot boot "+pathToTwrp)
    clear()
    input("Ok, now you need to wait a while, hit enter, when twrp will be booted")
    isBooted = input("Ok, so did twrp booted properly? Y/N ")
    if str.lower(isBooted) == "n":
        print(Fore.RED + "Make sure, that you downloaded proper recovery, also make sure that file is not damaged!"+Fore.RESET)
    print (Fore.GREEN+"Ok, so twrp booted, so now, we will install it"+Fore.RESET)
    os.system("adb reboot bootloader")
    os.system("fastboot flash recovery "+pathToTwrp)
    clear()
    print(Fore.GREEN+"So, everything went good, we are going back to twrp"+Fore.RESET)
    os.system("fastboot boot "+pathToTwrp)
    input("Press enter to continue")