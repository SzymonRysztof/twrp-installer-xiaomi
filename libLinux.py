import os
from sys import platform
import time
from libWindows import bcolors
clear = lambda: os.system('clear')
def installLinux():
    clear()
    twrpE = os.path.isfile('twrp.img')
    if twrpE == True:
        clear()
        os.system('fastboot devices')
        print (bcolors.OKBLUE+"Do you see your device here? (y/n): \n"+bcolors.ENDC)
        deviceVisible = input('');
        deviceVisible = deviceVisible.lower()
        if deviceVisible == "n":
            clear()
            print ("Check connection with device")
            print ("Phone should display MiTu rabbit \"Fixing\" android ")
            print ("And then you can restart this program")
            print()
            input("Press enter to continue")
            exit()
        elif deviceVisible == "y":
            clear()
            print (bcolors.OKGREEN+"Great! We can go to the next step\n"+bcolors.ENDC)
        else:
            clear()
            print (bcolors.FAIL+"You have to choose (Y)es or (N)o!"+bcolors.ENDC)
            installLinux()
        os.system('fastboot boot twrp.img')
        clear()
        print (bcolors.OKBLUE+"\nCan you see twrp screen on the phone (it can take some time, depending on the phone)(y/n)"+bcolors.ENDC)
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
    os.system('./main.py')
