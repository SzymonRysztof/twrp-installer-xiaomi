#!/usr/bin/python3
import os
import sys
import time
import urllib.request
#Thanks to stack overflow!
class bcolors:
    HEADER = '\033[95m'
    BL = '\033[94m'
    GR = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    W = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#this is path to /res/ folder and to .py file
#resPath = os.path.dirname(sys.executable)+os.sep+"res"+os.sep
resPath = os.path.abspath(os.path.dirname(__file__))+os.sep+"res"+os.sep
filePath = os.path.abspath(os.path.dirname(__file__))+os.sep
#filePath = os.path.dirname(sys.executable)+os.sep
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
    print (bcolors.BL+"\nThanks for using my software! check my repo \nhttps://github.com/mezutelni/twrp-installer-xiaomi \nto stay up to date!")
    print (bcolors.FAIL+"Also, if you like my job consider a donation for me so i could keep focusing on X.E.T\nhttps://www.paypal.me/Mezutelni \n"+bcolors.W)
    time.sleep(7)
    os.system("adb kill-server")
    sys.exit()
def mix2Cam():
	os.system("adb kill-server")
	os.system("adb shell mount /system")
	print (bcolors.WARN+"Don't worry if you see error here^ this means that your system is mounted already"+bcolors.W)
	os.system("adb shell mv /system/priv-app/MiuiCamera/MiuiCamera.apk /system/priv-app/MiuiCamera/MiuiCamera.apk.bak")
	isf = os.path.isfile(os.path.dirname(resPath)+os.sep +"cam.apk")
	if isf == False:
		print (bcolors.WARN+"I need to download camera file first, be patient please"+bcolors.W)
		urllib.request.urlretrieve('http://80.211.196.53/cam.apk', resPath+'cam.apk')
	elif isf == True:
		print (bcolors.GR+"Ok, you have camera file already!"+bcolors.W)
	os.system("adb push "+resPath+"cam.apk /system/priv-app/MiuiCamera/MiuiCamera.apk")
	os.system("adb shell chmod 644 /system/priv-app/MiuiCamera/MiuiCamera.apk")
	print (bcolors.BL+"Your old camera is still here, backed up, just in case")
	input("push enter to continue"+bcolors.W)
	sTweaksMenu()
def comMiuiHome():
    os.system("adb kill-server")
    os.system("adb shell mount /system")
    print (bcolors.WARN+"Don't worry if you see error here^ this means that your system is mounted already"+bcolors.W)
    os.system("adb shell mv /system/media/theme/default/com.miui.home /system/media/theme/default/com.miui.home.old")
    isf = os.path.isfile(os.path.dirname(resPath)+os.sep +"com.miui.home")
    if isf == False:
    	print (bcolors.WARN+"I need to download custom home file first, be patient please"+bcolors.W)
    	urllib.request.urlretrieve('http://80.211.196.53/home.file', resPath+'com.miui.home')
    elif isf == True:
    	print (bcolors.GR+"Ok, you have custom home file already!"+bcolors.W)
    os.system("adb push "+resPath+"com.miui.home /system/media/theme/default/com.miui.home")
    os.system("adb shell chmod 644 /system/media/theme/default/com.miui.home")
    print (bcolors.BL+"Your old com.miui.home is still here, backed up, just in case")
    input("push enter to continue"+bcolors.W)
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
	print ("Dpi has been changed!"+bcolors.W)
	os.system("adb kill-server")
	input("push enter to continue")
	sTweaksMenu()
def sideloader():
    while(True):
        print(bcolors.WARN+"Due to problems with adb sideload implementation, you have to start sideload on your phone manually!"+bcolors.W)
        sideloadFile = input(bcolors.BL+"Drag and drop your file here: "+bcolors.W)
        os.system("adb sideload "+sideloadFile)
        ifContinue = input("Do you want to sideload next file? (y/n)")
        ifContinue = str(ifContinue).lower()
        if ifContinue == 'n':
            print(bcolors.GR+"Ok, we'll go back now"+bcolors.W)
            input("Push enter to continue")
            menu()
        elif ifContinue =="y":
            print(bcolors.GR+"Ok! so here we go again"+bcolors.W)
        else:
            print (bcolors.FAIL+"Wrong option, so we will stop now, if u want to continue sideloading, just re launch this option from menu"+bcolors.W)
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
    	print (bcolors.FAIL+"You have to choose (Y)es or (N)o!"+bcolors.W)
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
    	print(bcolors.FAIL+"Wrong option!"+bcolors.W)
    	input("Push enter to continue")
    os.system('adb reboot bootloader')
    os.system('fastboot flash recovery twrp.img')
    os.system('fastboot boot twrp.img')
    print (bcolors.GR+"Please wait, +- 10s"+bcolors.W)
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
    	print (bcolors.FAIL+"You have to choose (Y)es or (N)o!"+bcolors.W)
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
    	print(bcolors.FAIL+"Wrong option!"+bcolors.W)
    	input("Push enter to continue")
    os.system('adb reboot bootloader')
    os.system('fastboot flash recovery '+path)
    os.system('fastboot boot '+path)
    print (bcolors.GR+"Please wait, +- 10s"+bcolors.W)
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
    print (bcolors.WARN+deviceN)
    print (bcolors.GR+"--------------------------------------------------------------------")
    print ("| X.E.T                                                            |")
    print ("| REBOOT MENU                                                      |")
    print ("| Some devices, like RN3P might have problems with reboots         |")
    print ("| from system, but reboots should work from adb/fastboot           |")
    print ("--------------------------------------------------------------------"+bcolors.W)
    print (bcolors.BOLD+"|1. Reboot to recovery                                             |")
    print (bcolors.WARN+"|Reboot to recovery using ADB (so make sure to turn on debugging)  |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|2. Reboot to fastboot                                             |")
    print (bcolors.WARN+"|Reboot to fastboot using ADB (so make sure to turn on debugging)  |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|3. Reboot to system                                               |")
    print (bcolors.WARN+"|Reboot to system using ADB (so make sure to turn on debugging)    |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|4. Reboot to system                                               |")
    print (bcolors.WARN+"|Reboot to system using Fastboot mode!                             |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|5. Reboot to adb-sideload                                         |")
    print (bcolors.WARN+"|Reboot to sideload using ADB-root (so use it when in recovery)    |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|0. Back to main menu                                              |")
    print (bcolors.BOLD+"--------------------------------------------------------------------"+bcolors.W)
    case = int(input(bcolors.BL+"choose: "+bcolors.W))
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
        print (bcolors.FAIL+"Error you should choose right option!"+bcolors.W)
        input("push enter to continue")
        rbMenu()
#System Tweaks Menu
def sTweaksMenu():
    clear()
    print (bcolors.WARN+deviceN)
    print (bcolors.GR+"--------------------------------------------------------------------")
    print ("| X.E.T                                                            |")
    print ("| SYSTEM TWEEKS MENU                                               |")
    print ("--------------------------------------------------------------------"+bcolors.W)
    print (bcolors.BOLD+"|1. Build.prop backup                                              |")
    print (bcolors.WARN+"|Use it to backup your build.prop file!                            |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|2. Build.prop restore                                             |")
    print (bcolors.WARN+"|Use it to restore your build.prop file!                           |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|3. Change DPI                                                     |")
    print (bcolors.WARN+"|For changing dpi more than once, you have to restore build.prop!  |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|4. Install mix 2 camera                                           |")
    print (bcolors.WARN+"|Mix 2 camera ported for all Xiaomi devices;Tested only on miui9   |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|5. Install modified com.miui.home (desktop grid up to 10x10)      |")
    print (bcolors.WARN+"|Miui 9 exclusive                                                  |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|6. Activate Camera 2 API                                          |")
    print (bcolors.WARN+"|Use it to activate cam2api in your build.prop                     |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|0. Back to main menu                                              |")
    print (bcolors.BOLD+"--------------------------------------------------------------------"+bcolors.W)
    case = int(input(bcolors.BL+"choose: "+bcolors.W))
    if case == 1:
        clear()
        os.system("adb shell mount /system")
        print ("Don't worry if you see error here^ this means that your system is mounted already")
        os.system("adb shell cp /system/build.prop /system/build.prop.bak")
        print (bcolors.GR+"Backup complete!"+bcolors.W)
        input("push enter to continue")
        sTweaksMenu()
    elif case == 2:
        clear()
        os.system("adb shell mount /system")
        print ("Don't worry if you see error here^ this means that your system is mounted already")
        os.system("adb shell cp /system/build.prop.bak /system/build.prop")
        print (bcolors.GR+"Restore complete!"+bcolors.W)
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
        os.system("adb shell \"persist.camera.HAL3.enabled=1 >> /system/build.prop\"")
        print ("You have enabled Camera 2 API YAY!")
        input("push enter to continue")
        sTweaksMenu()
    elif case==0:
        os.system("adb kill-server")
        clear()
        menu()
    else:
        clear()
        print (bcolors.FAIL+"Error you should choose right option!"+bcolors.W)
        input("push enter to continue")
        sTweaksMenu()
#Main Menu
def menu():
    clear()
    print (bcolors.WARN+deviceN)
    print (bcolors.GR+"--------------------------------------------------------------------")
    print ("| X.E.T                                                            |")
    print ("| Xiaomi Essential Tools                                           |")
    print ("--------------------------------------------------------------------"+bcolors.W)
    print (bcolors.BOLD+"|1. Reboot menu                                                    |")
    print (bcolors.WARN+"|Simple reboot menu, to make your life more comfortable!           |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|2. System tweaks                                                  |")
    print (bcolors.WARN+"|Here you can find system tweaks, they are all applied in recovery!|"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|3. Install Recovery                                               |")
    print (bcolors.WARN+"|Use it to install recovery                                        |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|4. Check bootloader status (locked/unlocked)                      |")
    print (bcolors.WARN+"|You have to be in fastboot mode to make it work                   |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|5. ADB sideloader                                                 |")
    print (bcolors.WARN+"|Start in recovery, then use it to flash all zips you want!        |"+bcolors.W)
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|7. Requirements                                                   |")
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|8. About me                                                       |")
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|9. Contact                                                        |")
    print (bcolors.BOLD+"--------------------------------------------------------------------")
    print (bcolors.BOLD+"|0. Exit                                                           |")
    print (bcolors.BOLD+"--------------------------------------------------------------------"+bcolors.W)
    case = int(input(bcolors.BL+"choose: "+bcolors.W))
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
    	print(bcolors.FAIL+"Error choose right option\n"+bcolors.W)
    	input("push enter to continue")
    	menu()
menu()
