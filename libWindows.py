import os
from sys import platform
import time
clear = lambda: os.system('cls')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
sPath = os.path.abspath(__file__)
def installWin():
    clear()
    twrpE = os.path.isfile(os.path.dirname(sPath)+os.sep +"twrp.img")
    if twrpE == True:
        clear()
        os.system('fastboot devices')
        print ("Do you see your device here? (y/n): \n")
        deviceVisible = input('');
        deviceVisible = deviceVisible.lower()
        if deviceVisible == "n":
            clear()
            print()
            print ("Check connection with device")
            print ("Phone should display MiTu rabbit \"Fixing\" android ")
            print ("And then you can restart this program")
            print()
            input("Press enter to continue")
            exit()
        elif deviceVisible == "y":
            clear()
            print ("Great! we can go to the next step\n")
        else:
            clear()
            print ("You have to choose (Y)es or (N)o!")
            print()
            installWin()
        os.system('fastboot boot twrp.img')
        clear()
        print ("\nCan you see twrp menu on your phone? (This can take some time, depending on the phone)(y/n)")
        twrpS = input().lower()
        if twrpS == "n":
            clear()
            print ("Make sure that: \n 1.You have twrp.img file in script root folder! \n 2.You have downloaded TWRP for YOUR phone \n ")
            print()
            input("Press enter to continue")
            exit()
        elif twrpS == "y":
            os.system('adb reboot bootloader')
            os.system('fastboot flash recovery twrp.img')
            os.system('fastboot boot twrp.img')
            print ("Please wait, +- 10s")
            time.sleep(10)
            os.system('adb reboot recovery')
    else:
        clear()
        print ("You dont have twrp.img in script root folder, dowload it first\nAnd put it this folder")
        print ()
        print ("https://twrp.me/Devices/")
        print()
        input("Press enter to continue")
        exit()
    clear()
    print ("Congratulations, your TWRP is ready to rock!")
    i = 5;
    print ("Going back to main menu in: ")
    while (i>0):
        print (i)
        i=i-1
        time.sleep(1)
    os.system("main.py")
