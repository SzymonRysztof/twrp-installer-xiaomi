#!/usr/bin/python3
import os
from sys import platform
from libLinux import installLinux
from libWindows import installWin, bcolors
import time


if platform == "linux" or platform == "linux2":
	clear = lambda: os.system('clear')
	s = "l"
elif platform == "win32":
	clear = lambda: os.system('cls')
	s = "w"
def bl():
	os.system('fastboot oem device-info > results.txt 2>&1')
	bl = open('results.txt', 'r').read()
	os.remove('results.txt')
	bl = bl[72]+bl[73]+bl[74]+bl[75]+bl[76]
	if bl[0] == "t":
		bl = "Unlocked"
	elif bl[0] == "f":
		bl = "Locked"
	print (bl)
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
	case = int(input("Choose: "))
	if case==1:
		clear()
		os.system('adb reboot recovery')
		rbMenu()
	elif case==2:
		clear()
		os.system('adb reboot bootloader')
		rbMenu()
	elif case==3:
		clear()
		os.system('adb reboot')
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
		rbMenu()
#Menu głowne programu!
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
	print ("|4. Requirements                                                   |")
	print ("--------------------------------------------------------------------")
	print ("|5. About me                                                       |")
	print ("--------------------------------------------------------------------")
	print ("|6. Contact                                                        |")
	print ("--------------------------------------------------------------------")
	print ("|0. Exit                                                           |")
	print ("--------------------------------------------------------------------")
	case = int(input(bcolors.OKBLUE+"choose: "+bcolors.ENDC))
	if case == 1:
		if platform == "linux" or platform == "linux2":
			installLinux()
		elif platform == "win32":
			installWin()
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
		clear()
		if s == "l":
			print("You have to install adb and fastboot package, in debian family you will propably just have to apt-get install, not sure about other distros\nAlso you have to make sure that your fastboot and adb is in /usr/bin/ \nYou can check it with whereis command")
		elif s=="w":
			print("You have to install minimal adb and fastboot with option system wide, thats it you should be good to go")
		input("push enter to continue")
		menu()
	elif case == 5:
		clear()
		print ("Script created by Mezutelni\n")
		print ("https://github.com/mezutelni/twrp-installer-xiaomi \n")
		input("push enter to continue")
		menu()
	elif case == 6:
		clear()
		print ("|My contact e-mail: \n----------------------------\n|mezutelni@gmail.com \n----------------------------\n|feel free to send me some feedback!\n")
		input("push enter to continue")
		menu()
	elif case == 0:
		exit()
	else:
		clear()
		print("Error choose right option\n")
		input("push enter to continue")
		menu()
menu()
