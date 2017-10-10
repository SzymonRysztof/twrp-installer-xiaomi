#!/usr/bin/python3
import os
from sys import platform
from libLinux import installLinux
from libWindows import installWin
import time
if platform == "linux" or platform == "linux2":
	clear = lambda: os.system('clear')
elif platform == "win32":
	clear = lambda: os.system('cls')
def bl():
	os.system('fastboot oem device-info > results.txt 2>&1')
	bl = open('results.txt', 'r').read()
	os.remove('results.txt')
	bl = bl[72]+bl[73]+bl[74]+bl[75]+bl[76]
	if bl[0] == "t":
		bl = "Odblokowany"
	elif bl[0] == "f":
		bl = "Zablokowany"
	print (bl)
def rbMenu():
	clear()
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|                                                                                                      |")
	print ("| REBOOT MENU                                                                                          |")
	print ("|                                                                                                      |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|1. Zrebootuj do Recovery (ADB)                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|2. Zrebootuj do Fastboot (ADB)                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|3. Zrebootuje do Systemu (ADB)                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|4. Zrebootuje do Systemu (Fastboot)                                                                   |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|0. Powrót do Menu głownego                                                                            |")
	print ("--------------------------------------------------------------------------------------------------------")
	case = int(input("Wybierz: "))
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
	elif case==0:
		clear()
		menu()
	else:
		clear()
		print ("Wybierz poprawną opcję!")
		rbMenu()
#Menu głowne programu!
def menu():
	clear()
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|                                                                                                      |")
	print ("| Witaj, ten prosty skrypt przeprowadzi Cię przez proces instalacji Recovery na twoim telefonie XIAOMI |")
	print ("|                                                                                                      |")
	print ("| Sugeruje rozszerzenie okna konsoli dla lepszych odczuć                                               |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|1. Instaluj Recovery                                                                                  |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|2. Reboot menu                                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|3. Sprawdź status Bootloadera (l/u)                                                                   |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|4. Wymagania                                                                                          |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|5. O Autorze                                                                                          |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|6. Kontakt                                                                                            |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|0. Wyjście                                                                                            |")
	print ("--------------------------------------------------------------------------------------------------------")
	case = int(input("Wybierz: "))
	if case == 1:
		if platform == "linux" or platform == "linux2":
			installLinux()
		elif platform == "win32":
			installWin()
	elif case == 2:
		rbMenu()
	elif case == 3:
		clear()
		print ("--------------------------------------------------------------------------------------------------------")
		print ("Status odblokowanie twojego bootloader to:                                                              ")
		bl()
		print ("--------------------------------------------------------------------------------------------------------")
		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 4:
		clear()
		print("Wymagania: \n 1. Adb i Fastboot poprawnie zainstalowane \n 2. Plik twrp.img znajdujący się w katalogu ze skrptem \n 3. Python w wersji 3 \n 4. Odblokowany bootloader")
		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 5:
		clear()
		print ("About me")
		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 6:
		clear()
		print ("Contact")
		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 0:
		exit()
	else:
		clear()
		print("Wybierz poprawną opcję!\n")
		input("wcisnij enter aby kontynuowac")
		menu()
menu()
