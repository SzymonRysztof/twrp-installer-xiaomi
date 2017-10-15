#!/usr/bin/python3
import os
from sys import platform
from sys import exit
import time
import urllib.request
import signal

#some variables to make this script work fine
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
resPath = os.path.abspath(os.path.dirname(__file__))+os.sep+"res"+os.sep
filePath = os.path.abspath(os.path.dirname(__file__))+os.sep
if platform == "linux" or platform == "linux2":
	clear = lambda: os.system('clear')
	s = "l"
elif platform == "win32":
	clear = lambda: os.system('cls')
	s = "w"

#all functions
def goodbye():
    print ("\nThanks for using my software! check my repo \nhttps://github.com/mezutelni/twrp-installer-xiaomi \nto stay up to date!")
    time.sleep(5)
    exit()
def twrpDownloader():
	device = os.system("adb shell \"cat /system/build.prop | grep ro.product.device=\" > tmp ")
	device = open('tmp', 'r').read()
	open('tmp', "r").close()
	device = device.lstrip('ro.product.device')[1:]
	device = ''.join(device.split())
	urllib.request.urlretrieve('http://80.211.196.53/'+device+'.img', resPath+'twrp.img')
def mix2Cam():
	os.system("adb kill-server")
	os.system("adb shell mount /system")
	print ("Don't worry if you see error here^ this means that your system is mounted already")
	os.system("adb shell mv /system/priv-app/MiuiCamera/MiuiCamera.apk /system/priv-app/MiuiCamera/MiuiCamera.apk.bak")
	isf = os.path.isfile(os.path.dirname(resPath)+os.sep +"cam.apk")
	if isf == False:
		print ("I need to download camera file first, be patient pls")
		urllib.request.urlretrieve('http://80.211.196.53/cam.apk', resPath+'cam.apk')
	elif isf == True:
		print ("Ok, you have camera file already!")
	os.system("adb push "+resPath+"cam.apk /system/priv-app/MiuiCamera/MiuiCamera.apk")
	os.system("adb shell chmod 644 /system/priv-app/MiuiCamera/MiuiCamera.apk")
	print ("Your old camera is still here, backed up, just in case")
	input("push enter to continue")
	sTweaksMenu()
def comMiuiHome():
    os.system("adb kill-server")
    os.system("adb shell mount /system")
    print ("Don't worry if you see error here^ this means that your system is mounted already")
    os.system("adb shell mv /system/media/theme/default/com.miui.home /system/media/theme/default/com.miui.home.old")
    isf = os.path.isfile(os.path.dirname(resPath)+os.sep +"com.miui.home")
    if isf == False:
    	print ("I need to download custom home file first, be patient pls")
    	urllib.request.urlretrieve('http://80.211.196.53/home.file', resPath+'com.miui.home')
    elif isf == True:
    	print ("Ok, you have custom home file already!")
    os.system("adb push "+resPath+"com.miui.home /system/media/theme/default/com.miui.home")
    os.system("adb shell chmod 644 /system/media/theme/default/com.miui.home")
    print ("Your old com.miui.home is still here, backed up, just in case")
    input("push enter to continue")
    sTweaksMenu()
def bl():
	os.system('fastboot oem device-info > results.txt 2>&1')
	bl = open('results.txt', 'r').read()
	os.remove('results.txt')
	#bl = bl[72]+bl[73]+bl[74]+bl[75]+bl[76]
	if bl[72] == "t":
		bl = "Unlocked"
	elif bl[72] == "f":
		bl = "Locked"
	print (bl)
def dpiChanger():
	os.system("adb shell mount /system")
	print ("Make sure that you made a build.prop backup! just in case")
	dpi = input("Tell me what is your desired dpi: ")
	os.system("adb shell \"echo \\\"ro.sf.lcd_density = "+dpi+"\\\" >> /system/build.prop\"")
	print ("Dpi has been changed!"+bcolors.ENDC)
	os.system("adb kill-server")
	input("push enter to continue")
	sTweaksMenu()
def twrpInstall():
	clear()
	os.system("adb start-server")
	print("First, i have to download TWRP for you, make sure that your phone is turned on")
	input("Push enter to continue")
	device = os.system("adb shell \"cat /system/build.prop | grep ro.product.device=\" > tmp ")
	device = open('tmp', 'r').read()
	open('tmp', "r").close()
	os.remove("tmp")
	device = device.lstrip('ro.product.device')[1:]
	device = ''.join(device.split())
	print ("So, your device is "+device+", be patient file is now being downloaded")
	urllib.request.urlretrieve('http://80.211.196.53/'+device+'.img', filePath+'twrp.img')
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
		print ("You have to choose (Y)es or (N)o!")
		print()
		twrpInstall()

	os.system('fastboot boot twrp.img')
	clear()
	print ("\nCan you see twrp menu on your phone? (This can take some time, depending on the phone)(y/n)")
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
		print("Wrong option!")
		input("Push enter to continue")
	os.system('adb reboot bootloader')
	os.system('fastboot flash recovery twrp.img')
	os.system('fastboot boot twrp.img')
	print ("Please wait, +- 10s")
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

#Reboot Menu
def rbMenu():
	clear()
	print (bcolors.OKGREEN+"--------------------------------------------------------------------")
	print ("| X.E.T                                                            |")
	print ("| REBOOT MENU                                                      |")
	print ("--------------------------------------------------------------------"+bcolors.ENDC)
	print ("|1. Reboot to recovery (via ADB)                                   |")
	print ("--------------------------------------------------------------------")
	print ("|2. Reboot to fastboot (via ADB)                                   |")
	print ("--------------------------------------------------------------------")
	print ("|3. Reboot to system (via ADB)                                     |")
	print ("--------------------------------------------------------------------")
	print ("|4. Reboot to system (via Fastboot)                                |")
	print ("--------------------------------------------------------------------")
	print ("|0. Back to main menu                                              |")
	print ("--------------------------------------------------------------------")
	case = int(input(bcolors.OKBLUE+"choose: "+bcolors.ENDC))
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
	elif case==0:
		clear()
		menu()
	else:
		clear()
		print ("Error you should choose right option!")
		input("push enter to continue")
		rbMenu()
#System Tweaks Menu
def sTweaksMenu():
	clear()
	print (bcolors.OKGREEN+"--------------------------------------------------------------------")
	print ("| X.E.T                                                            |")
	print ("| SYSTEM TWEEKS MENU                                               |")
	print ("| They are all made in recovery(so you can stay rootless)!         |")
	print ("--------------------------------------------------------------------"+bcolors.ENDC)
	print ("|1. Build.prop backup                                              |")
	print ("--------------------------------------------------------------------")
	print ("|2. Build.prop restore                                             |")
	print ("--------------------------------------------------------------------")
	print ("|3. Change DPI                                                     |")
	print ("--------------------------------------------------------------------")
	print ("|4. Install mix 2 camera                                           |")
	print ("--------------------------------------------------------------------")
	print ("|5. Install modified com.miui.home (desktop grid up to 10x10)      |")
	print ("--------------------------------------------------------------------")
	print ("|6. Activate Camera 2 API                                          |")
	print ("--------------------------------------------------------------------")
	print ("|0. Back to main menu                                              |")
	print ("--------------------------------------------------------------------")
	case = int(input(bcolors.OKBLUE+"choose: "+bcolors.ENDC))
	if case == 1:
		os.system("adb shell mount /system")
		print ("Don't worry if you see error here^ this means that your system is mounted already")
		os.system("adb shell cp /system/build.prop /system/build.prop.bak")
		print (bcolors.OKGREEN+"Backup complete!"+bcolors.ENDC)
		input("push enter to continue")
		sTweaksMenu()
	elif case == 2:
		os.system("adb shell mount /system")
		print ("Don't worry if you see error here^ this means that your system is mounted already")
		os.system("adb shell cp /system/build.prop.bak /system/build.prop")
		print (bcolors.OKGREEN+"Restore complete!"+bcolors.ENDC)
		input("push enter to continue")
		sTweaksMenu()
	elif case == 3:
		dpiChanger()
	elif case == 4:
		mix2Cam()
	elif case == 5:
		comMiuiHome()
	elif case == 6:
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
		print ("Error you should choose right option!")
		input("push enter to continue")
		sTweaksMenu()
#Main Menu
def menu():
	clear()
	print (bcolors.OKGREEN+"--------------------------------------------------------------------")
	print ("| X.E.T                                                            |")
	print ("| Xiaomi Essential Tools                                           |")
	print ("--------------------------------------------------------------------"+bcolors.ENDC)
	print ("|1. Install Recovery                                               |")
	print ("--------------------------------------------------------------------")
	print ("|2. Reboot menu                                                    |")
	print ("--------------------------------------------------------------------")
	print ("|3. Check bootloader status (locked/unlocked)                      |")
	print ("--------------------------------------------------------------------")
	print ("|4. System tweaks                                                  |")
	print ("--------------------------------------------------------------------")
	print ("|7. Requirements                                                   |")
	print ("--------------------------------------------------------------------")
	print ("|8. About me                                                       |")
	print ("--------------------------------------------------------------------")
	print ("|9. Contact                                                        |")
	print ("--------------------------------------------------------------------")
	print ("|0. Exit                                                           |")
	print ("--------------------------------------------------------------------")
	case = int(input(bcolors.OKBLUE+"choose: "+bcolors.ENDC))
	if case == 1:
		os.system("adb kill-server")
		twrpInstall()
	elif case == 2:
		rbMenu()
	elif case == 3:
		clear()
		print ("--------------------------------------------------------------------")
		print ("Your bootloader status is: ")
		bl()
		print ("--------------------------------------------------------------------")
		input("push enter to continue")
		menu()
	elif case == 4:
		sTweaksMenu()
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
		print("Error choose right option\n")
		input("push enter to continue")
		menu()
menu()
#ctrl+c handler
signal.signal(signal.SIGINT, lambda number, frame: goodbye())
