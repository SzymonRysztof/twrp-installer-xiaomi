#!/usr/bin/python3
import os
import sys
import time
import urllib.request
from colorama import Fore, Back, Style, init
#Thanks to stack overflow!
init()
"""class bcolors:
    HEADER = '\033[95m'
    BL = '\033[94m'
    GR = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    W = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
"""
#this is path to /res/ folder and to .py file
resPath = os.path.dirname(sys.executable)+os.sep+"res"+os.sep
filePath = os.path.dirname(sys.executable)+os.sep
#here i'm checking wchich os you are using and setting command to clear cmd/terminal window
if sys.platform == "linux" or sys.platform == "linux2":
	clear = lambda: os.system('clear')
	s = "l"
elif sys.platform == "win32":
	clear = lambda: os.system('cls')
	s = "w"
#this is list of devices with official twrp support
supported_devices=["aries","cancro","capricorn","dior","ferrari","gemini","helium","hennessy","hermes","hydrogen","ido","kate","kenzo","land","libra","lithium","mido","mocha","natrium","rolex","sagit","santoni"]
devices=["cancro","libra","ferrari","aqua","gemini","virgo","leo","scorpio","jason","tiffany","song","meri","tisson","capricorn","natrium","lithium","chiron","sagit","hydrogen","oxygen","helium","HM2013023","armani","HM2014811","HM2014813","omega","lcsh92_wet_jb9","gucci","dior","hermes","ido","land","hennessy","kate","kenzo","nikel","prada","markw","ugg","mido","rolex","santoni","mocha","latte","cappu",]
supported_devicesDict ={
#mi
"aries":"Mi 2",
"pisces":"Mi 3 TD",
"cancro":"Mi 3 W/Mi 4",
"libra":"Mi 4c",
"ferrari":"Mi 4i",
"aqua":"Mi 4s",
"gemini":"Mi 5",
"virgo":"Mi Note",
"leo":"Mi Note Pro",
"scorpio":"Mi Note 2",
"jason":"Mi Note 3",
"tiffany":"Mi 5x",
"song":"Mi 5c",
"meri":"Mi 5c",
"tisson":"Mi A1",
"capricorn":"Mi 5s",
"natrium":"Mi 5s+",
"lithium":"Mi MIX",
"chiron":"Mi MIX 2",
"sagit":"Mi 6",
"hydrogen":"Mi MAX",
"oxygen":"Mi MAX 2",
"helium":"Mi MAX PRO",
#Redmi
"HM2013023":"Redmi 1 - WCDMA",
"armani":"Redmi 1s - WCDMA",
"HM2014811":"Redmi 2 - WCDMA",
"HM2014813":"Redmi 2 - TD",
"omega":"Redmi PRO",
"lcsh92_wet_jb9":"Redmi note 1 - 3g-mtk",
"gucci":"Redmi note 1s",
"dior":"Redmi Note 1 - 4g",
"hermes":"Redmi Note 2",
"ido":"Redmi 3",
"land":"Redmi 3 S/X",
"hennessy":"Redmi Note 3 (MTK)",
"kate":"Redmi Note 3 Global",
"kenzo":"Redmi Note 3 Chinese",
"nikel":"Redmi Note 4",
"prada":"Redmi 4",
"markw":"Redmi 4 pro",
"ugg":"Redmi Note 5A",
"mido":"Redmi Note 4x",
"rolex":"Redmi 4a",
"santoni":"Redmi 4x",
#Tablets
"mocha":"Mi PAD",
"latte":"Mi PAD 2",
"cappu":"Mi PAD 3",
}
os.system("adb start-server")
glob_device = os.system("adb shell \"cat /system/build.prop | grep ro.product.device=\" > tmp ")
glob_device = open('tmp', 'r').read()
open('tmp', "r").close()
os.remove("tmp")
glob_device = glob_device.lstrip('ro.product.device')[1:]
glob_device = ''.join(glob_device.split())
tf = 0
i = 0
i = int(i)
for i in range(len(devices)):
    if glob_device == devices[i]:
        deviceN = supported_devicesDict[devices[i]]
        break
    elif glob_device != devices[i]:
        deviceN = "Device Not Connected"
#Here are all functions that i'm using below (not all options in menu are functions)
def goodbye():
    print (Fore.BLUE+"\nThanks for using my software! check my repo \nhttps://github.com/mezutelni/twrp-installer-xiaomi \nto stay up to date!")
    print (Fore.RED+"Also, if you like my job consider a donation for me so i could keep focusing on X.E.T\nhttps://www.paypal.me/Mezutelni \n"+Style.RESET_ALL)
    time.sleep(7)
    os.system("adb kill-server")
    sys.exit()
def mix2Cam():
	os.system("adb kill-server")
	os.system("adb shell mount /system")
	print (Fore.YELLOW+"Don't worry if you see error here^ this means that your system is mounted already"+Style.RESET_ALL)
	os.system("adb shell mv /system/priv-app/MiuiCamera/MiuiCamera.apk /system/priv-app/MiuiCamera/MiuiCamera.apk.bak")
	isf = os.path.isfile(os.path.dirname(resPath)+os.sep +"cam.apk")
	if isf == False:
		print (Fore.YELLOW+"I need to download camera file first, be patient please"+Style.RESET_ALL)
		urllib.request.urlretrieve('http://80.211.196.53/cam.apk', resPath+'cam.apk')
	elif isf == True:
		print (Fore.GREEN+"Ok, you have camera file already!"+Style.RESET_ALL)
	os.system("adb push "+resPath+"cam.apk /system/priv-app/MiuiCamera/MiuiCamera.apk")
	os.system("adb shell chmod 644 /system/priv-app/MiuiCamera/MiuiCamera.apk")
	print (Fore.BLUE+"Your old camera is still here, backed up, just in case")
	input("push enter to continue"+Style.RESET_ALL)
	sTweaksMenu()
def comMiuiHome():
    os.system("adb kill-server")
    os.system("adb shell mount /system")
    print (Fore.YELLOW+"Don't worry if you see error here^ this means that your system is mounted already"+Style.RESET_ALL)
    os.system("adb shell mv /system/media/theme/default/com.miui.home /system/media/theme/default/com.miui.home.old")
    isf = os.path.isfile(os.path.dirname(resPath)+os.sep +"com.miui.home")
    if isf == False:
    	print (Fore.YELLOW+"I need to download custom home file first, be patient please"+Style.RESET_ALL)
    	urllib.request.urlretrieve('http://80.211.196.53/home.file', resPath+'com.miui.home')
    elif isf == True:
    	print (Fore.GREEN+"Ok, you have custom home file already!"+Style.RESET_ALL)
    os.system("adb push "+resPath+"com.miui.home /system/media/theme/default/com.miui.home")
    os.system("adb shell chmod 644 /system/media/theme/default/com.miui.home")
    print (Fore.BLUE+"Your old com.miui.home is still here, backed up, just in case")
    input("push enter to continue"+Style.RESET_ALL)
    sTweaksMenu()
def bl():
    print ("To make this work, you have to be in fastboot mode!")
    print ("Do you want to continue? (Y/N)")
    x = input("")
    clear()
    if x.lower() == "y":
        print ("Your bootloader status is: ")
        os.system('fastboot oem device-info > results.txt 2>&1')
        bl = open('results.txt', 'r').read()
        os.remove('results.txt')
        #bl = bl[72]+bl[73]+bl[74]+bl[75]+bl[76]
        if bl[72] == "t":
            bl = "Unlocked"
        elif bl[72] == "f":
            bl = "Locked"
        print (bl)
    elif x.lower() == "n":
        menu()
def dpiChanger():
	os.system("adb shell mount /system")
	print ("Make sure that you made a build.prop backup! just in case")
	dpi = input("Tell me what is your desired dpi: ")
	os.system("adb shell \"echo \\\"ro.sf.lcd_density = "+dpi+"\\\" >> /system/build.prop\"")
	print ("Dpi has been changed!"+Style.RESET_ALL)
	os.system("adb kill-server")
	input("push enter to continue")
	sTweaksMenu()
def sideloader():
    while(True):
        print(Fore.YELLOW+"Due to problems with adb sideload implementation, you have to start sideload on your phone manually!"+Style.RESET_ALL)
        sideloadFile = input(Fore.BLUE+"Drag and drop your file here: "+Style.RESET_ALL)
        os.system("adb sideload "+sideloadFile)
        ifContinue = input("Do you want to sideload next file? (y/n)")
        ifContinue = str(ifContinue).lower()
        if ifContinue == 'n':
            print(Fore.GREEN+"Ok, we'll go back now"+Style.RESET_ALL)
            input("Push enter to continue")
            menu()
        elif ifContinue =="y":
            print(Fore.GREEN+"Ok! so here we go again"+Style.RESET_ALL)
        else:
            print (Fore.RED+"Wrong option, so we will stop now, if u want to continue sideloading, just re launch this option from menu"+Style.RESET_ALL)
            time.sleep(5)
            menu()
def twrpInstall():
    clear()
    print("First, i have to download TWRP for you, make sure that your phone is turned on")
    input("Push enter to continue")
    device = os.system("adb shell \"cat /system/build.prop | grep ro.product.device=\" > tmp ")
    device = open('tmp', 'r').read()
    open('tmp', "r").close()
    os.remove("tmp")
    device = device.lstrip('ro.product.device')[1:]
    device = ''.join(device.split())
    tf = 0
    i = 0
    i = int(i)
    array_length = len(supported_devices)
    for i in range(array_length):
        if device == supported_devices[i]:
            tf = True
            break
        elif device != supported_devices[i]:
            tf  = False
    if tf == True:
        urllib.request.urlretrieve('http://80.211.196.53/twrps/'+device+'.img', resPath+'twrp.img')
    elif tf == False:
        clear()
        print("Sadly, there is no Official TWRP for your "+supported_devicesDict[device]+" so you will have to download image manually :(")
        install = input("Do you want to install downloaded image now? (Y/N)")
        if install.lower() == "y":
            manualTwrp()
        else:
            menu()

    print ("So, your device is "+supported_devicesDict[device]+", be patient file is now being downloaded")
    urllib.request.urlretrieve('http://80.211.196.53/twrps/'+device+'.img', filePath+'twrp.img')
    os.system("adb reboot bootloader")
    time.sleep(5)
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
    	goodbye()

    elif deviceVisible == "y":
    	clear()
    	print ("Great! we can go to the next step\n")

    else:
    	clear()
    	print (Fore.RED+"You have to choose (Y)es or (N)o!"+Style.RESET_ALL)
    	print()
    	twrpInstall()

    os.system('fastboot boot twrp.img')
    clear()
    print ("\nCan you see twrp menu on your phone? (This can take some time, depending on the phone\nAlso you should wait for full boot!)(y/n)")
    twrpS = input().lower()

    if twrpS == "n":
    	clear()
    	print ("If you have benn waiting longer than 1min you should contact me first\n")
    	print ("For now, we are going back to main menu!")
    	input("Push enter to continue")
    	menu()
    elif twrpS == "y":
    	print("Ok, here we go!")

    else:
    	print(Fore.RED+"Wrong option!"+Style.RESET_ALL)
    	input("Push enter to continue")
    os.system('adb reboot bootloader')
    os.system('fastboot flash recovery twrp.img')
    os.system('fastboot boot twrp.img')
    print (Fore.GREEN+"Please wait, +- 10s"+Style.RESET_ALL)
    time.sleep(10)
    os.system('adb reboot recovery')
    clear()
    print ("Congratulations, your TWRP is ready to rock!")
    i = 5;
    print ("Going back to main menu in: ")
    while (i>0):
    	print (i)
    	i=i-1
    	time.sleep(1)
    os.remove(resPath+'twrp.img')
    menu()
def manualTwrp():
    path = input("Drag and drop img here! ")
    device = os.system("adb shell \"cat /system/build.prop | grep ro.product.device=\" > tmp ")
    device = open('tmp', 'r').read()
    open('tmp', "r").close()
    os.remove("tmp")
    device = device.lstrip('ro.product.device')[1:]
    device = ''.join(device.split())
    os.system("adb reboot bootloader")
    time.sleep(5)
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
    	goodbye()

    elif deviceVisible == "y":
    	clear()
    	print ("Great! we can go to the next step\n")

    else:
    	clear()
    	print (Fore.RED+"You have to choose (Y)es or (N)o!"+Style.RESET_ALL)
    	print()
    	twrpInstall()

    os.system('fastboot boot '+path)
    clear()
    print ("\nCan you see twrp menu on your phone? (This can take some time, depending on the phone\nAlso you should wait for full boot!)(y/n)")
    twrpS = input().lower()

    if twrpS == "n":
    	clear()
    	print ("If you have benn waiting longer than 1min you should contact me first\n")
    	print ("For now, we are going back to main menu!")
    	input("Push enter to continue")
    	menu()
    elif twrpS == "y":
    	print("Ok, here we go!")

    else:
    	print(Fore.RED+"Wrong option!"+Style.RESET_ALL)
    	input("Push enter to continue")
    os.system('adb reboot bootloader')
    os.system('fastboot flash recovery '+path)
    os.system('fastboot boot '+path)
    print (Fore.GREEN+"Please wait, +- 10s"+Style.RESET_ALL)
    time.sleep(10)
    os.system('adb reboot recovery')
    clear()
    print ("Congratulations, your TWRP is ready to rock!")
    i = 5;
    print ("Going back to main menu in: ")
    while (i>0):
    	print (i)
    	i=i-1
    	time.sleep(1)
    menu()
#Reboot Menu
def rbMenu():
    clear()
    print (Fore.YELLOW+deviceN)
    print (Fore.GREEN+"--------------------------------------------------------------------")
    print ("| X.E.T                                                            |")
    print ("| REBOOT MENU                                                      |")
    print ("| Some devices, like RN3P might have problems with reboots         |")
    print ("| from system, but reboots should work from adb/fastboot           |")
    print ("--------------------------------------------------------------------"+Style.RESET_ALL)
    print (Fore.CYAN+"|1. Reboot to recovery                                             |")
    print (Fore.YELLOW+"|Reboot to recovery using ADB (so make sure to turn on debugging)  |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|2. Reboot to fastboot                                             |")
    print (Fore.YELLOW+"|Reboot to fastboot using ADB (so make sure to turn on debugging)  |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|3. Reboot to system                                               |")
    print (Fore.YELLOW+"|Reboot to system using ADB (so make sure to turn on debugging)    |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|4. Reboot to system                                               |")
    print (Fore.YELLOW+"|Reboot to system using Fastboot mode!                             |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|5. Reboot to adb-sideload                                         |")
    print (Fore.YELLOW+"|Reboot to sideload using ADB-root (so use it when in recovery)    |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|0. Back to main menu                                              |")
    print (Fore.CYAN+"--------------------------------------------------------------------"+Style.RESET_ALL)
    case = int(input(Fore.BLUE+"choose: "+Style.RESET_ALL))
    if case==1:
        clear()
        os.system('adb reboot recovery')
        os.system('adb kill-server')
        rbMenu()
    elif case==2:
        clear()
        os.system('adb reboot bootloader')
        os.system('adb kill-server')
        rbMenu()
    elif case==3:
        clear()
        os.system('adb reboot')
        os.system('adb kill-server')
        rbMenu()
    elif case==4:
        clear()
        os.system('fastboot reboot')
        menu()
    elif case==5:
        clear()
        os.system('adb reboot sideload')
        menu()
    elif case==0:
        clear()
        menu()
    else:
        clear()
        print (Fore.RED+"Error you should choose right option!"+Style.RESET_ALL)
        input("push enter to continue")
        rbMenu()
#System Tweaks Menu
def sTweaksMenu():
    clear()
    print (Fore.YELLOW+deviceN)
    print (Fore.GREEN+"--------------------------------------------------------------------")
    print ("| X.E.T                                                            |")
    print ("| SYSTEM TWEEKS MENU                                               |")
    print ("--------------------------------------------------------------------"+Style.RESET_ALL)
    print (Fore.CYAN+"|1. Build.prop backup                                              |")
    print (Fore.YELLOW+"|Use it to backup your build.prop file!                            |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|2. Build.prop restore                                             |")
    print (Fore.YELLOW+"|Use it to restore your build.prop file!                           |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|3. Change DPI                                                     |")
    print (Fore.YELLOW+"|For changing dpi more than once, you have to restore build.prop!  |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|4. Install mix 2 camera                                           |")
    print (Fore.YELLOW+"|Mix 2 camera ported for all Xiaomi devices;Tested only on miui9   |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|5. Install modified com.miui.home (desktop grid up to 10x10)      |")
    print (Fore.YELLOW+"|Miui 9 exclusive                                                  |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|6. Activate Camera 2 API                                          |")
    print (Fore.YELLOW+"|Use it to activate cam2api in your build.prop                     |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|0. Back to main menu                                              |")
    print (Fore.CYAN+"--------------------------------------------------------------------"+Style.RESET_ALL)
    case = int(input(Fore.BLUE+"choose: "+Style.RESET_ALL))
    if case == 1:
        clear()
        os.system("adb shell mount /system")
        print ("Don't worry if you see error here^ this means that your system is mounted already")
        os.system("adb shell cp /system/build.prop /system/build.prop.bak")
        print (Fore.GREEN+"Backup complete!"+Style.RESET_ALL)
        input("push enter to continue")
        sTweaksMenu()
    elif case == 2:
        clear()
        os.system("adb shell mount /system")
        print ("Don't worry if you see error here^ this means that your system is mounted already")
        os.system("adb shell cp /system/build.prop.bak /system/build.prop")
        print (Fore.GREEN+"Restore complete!"+Style.RESET_ALL)
        input("push enter to continue")
        sTweaksMenu()
    elif case == 3:
        clear()
        dpiChanger()
    elif case == 4:
        clear()
        mix2Cam()
    elif case == 5:
        clear()
        comMiuiHome()
    elif case == 6:
        clear()
        os.system("adb shell mount /system")
        print ("Don't worry if you see error here^ this means that your system is mounted already")
        os.system('adb shell "echo persist.camera.HAL3.enabled=1 >> /system/build.prop"')
        print ("You have enabled Camera 2 API YAY!")
        input("push enter to continue")
        sTweaksMenu()
    elif case==0:
        os.system("adb kill-server")
        clear()
        menu()
    else:
        clear()
        print (Fore.RED+"Error you should choose right option!"+Style.RESET_ALL)
        input("push enter to continue")
        sTweaksMenu()
#Main Menu
def menu():
    clear()
    print (Fore.YELLOW+deviceN)
    print (Fore.GREEN+"--------------------------------------------------------------------")
    print ("| X.E.T                                                            |")
    print ("| Xiaomi Essential Tools                                           |")
    print ("--------------------------------------------------------------------"+Style.RESET_ALL)
    print (Fore.CYAN+"|1. Reboot menu                                                    |")
    print (Fore.YELLOW+"|Simple reboot menu, to make your life more comfortable!           |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|2. System tweaks                                                  |")
    print (Fore.YELLOW+"|Here you can find system tweaks, they are all applied in recovery!|"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|3. Install Recovery                                               |")
    print (Fore.YELLOW+"|Use it to install recovery                                        |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|4. Check bootloader status (locked/unlocked)                      |")
    print (Fore.YELLOW+"|You have to be in fastboot mode to make it work                   |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|5. ADB sideloader                                                 |")
    print (Fore.YELLOW+"|Start in recovery, then use it to flash all zips you want!        |"+Style.RESET_ALL)
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|7. Requirements                                                   |")
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|8. About me                                                       |")
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|9. Contact                                                        |")
    print (Fore.CYAN+"--------------------------------------------------------------------")
    print (Fore.CYAN+"|0. Exit                                                           |")
    print (Fore.CYAN+"--------------------------------------------------------------------"+Style.RESET_ALL)
    case = int(input(Fore.BLUE+"choose: "+Style.RESET_ALL))
    if case == 1:
    	rbMenu()
    elif case == 2:
        sTweaksMenu()
    elif case == 3:
        twrpInstall()
    elif case == 4:
    	clear()
    	bl()
    	input("push enter to continue")
    	menu()
    elif case == 5:
        os.system("adb kill-server")
        clear()
        sideloader()
    elif case == 7:
    	clear()
    	if s == "l":
    		print("You have to install adb and fastboot package, in debian family you will propably just have to apt-get install, not sure about other distros\nAlso you have to make sure that your fastboot and adb is in /usr/bin/ \nYou can check it with whereis command")
    	elif s=="w":
    		print("You have to install minimal adb and fastboot with option system wide, thats it you should be good to go")
    	input("push enter to continue")
    	menu()
    elif case == 8:
    	clear()
    	print ("Script created by Mezutelni\n")
    	print ("https://github.com/mezutelni/twrp-installer-xiaomi \n")
    	input("push enter to continue")
    	menu()
    elif case == 9:
    	clear()
    	print ("|My contact e-mail: \n----------------------------\n|mezutelni@gmail.com \n----------------------------\n|feel free to send me some feedback!\n")
    	input("push enter to continue")
    	menu()
    elif case == 0:
    	goodbye()
    else:
    	clear()
    	print(Fore.RED+"Error choose right option\n"+Style.RESET_ALL)
    	input("push enter to continue")
    	menu()
menu()
