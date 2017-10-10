#!/usr/bin/python3
import os
from sys import platform
import linux
import windows
import time

    clear = os.system("clear")

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

#ta funkcja sprawdza czy zainstalowany jest fastboot w linuxie

def chckfl():
	f = os.path.isfile('/usr/bin/fastboot')
	a = os.path.isfile('/usr/bin/adb')
	if f == True and a == True:
		return True
	elif f == True and a == False:
		print ("Nie znaleziono pliku binarnego adb w '/usr/bin'")
		print ("Nie można dokończyć działania programu!")
        menu()
	elif f == False and a == True:
		print ("Nie znaleziono pliku binarnego Fastboot w '/usr/bin'")
		print ("Nie można dokończyć działania programu!")
        menu()
	elif f == False and a == False:
		print ("Nie znaleziono plików binarnych Fastboot i Adb w '/usr/bin'")
		print ("Nie można dokończyć działania programu!")
        menu()
	else:
		print ("Nieznany błąd! kończe działanie programu!")
		exit()
#Ta funckja odpowiada za proces instalacji na linuxie

#Menu głowne programu!
def menu():
	 
	clear
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|                                                                                                      |")
	print ("| Witaj, ten prosty skrypt przeprowadzi Cię przez proces instalacji Recovery na twoim telefonie XIAOMI |")
	print ("|                                                                                                      |")
	print ("| Sugeruje rozszerzenie okna konsoli dla lepszych odczuć                                               |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|1. Instaluj Recovery                                                                                  |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|2. Zrebootuj do Recovery (ADB)                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|3. Zrebootuj do Fastboot (ADB)                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|4. Zrebootuje do Systemu (ADB)                                                                        |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|5. Zrebootuje do Systemu (Fastboot)                                                                   |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|6. Sprawdź status Bootloadera (l/u)                                                                   |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|7. Wymagania                                                                                          |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|8. O Autorze                                                                                          |")
	print ("--------------------------------------------------------------------------------------------------------")
	print ("|9. Kontakt                                                                                            |")
	print ("--------------------------------------------------------------------------------------------------------")
    print ("|0. Wyjście                                                                                            |")
	print ("--------------------------------------------------------------------------------------------------------")
	case = int(input("Wybierz: "))
	if case == 1
        if platform == "linux" or platform == "linux2":
            linux.installLinux()
        #elif platform == "win32":
            #windows.installWin()
    elif case == 2:
		os.system('adb reboot recovery')
		menu()
	elif case == 3:
		os.system('adb reboot bootloader')
		menu()
	elif case == 4:
		os.system('adb reboot')
		print("")
		menu()
	elif case == 5:
		os.system('fastboot reboot')
		print("")
		menu()
	elif case == 6:
		 
		clear
		print ("--------------------------------------------------------------------------------------------------------")
		print ("Status odblokowanie twojego bootloader to:                                                              ")
		bl()
		print ("--------------------------------------------------------------------------------------------------------")

		input("wcisnij enter aby kontynuowac")
		menu()

	elif case == 7:
		 
		clear
		print("Wymagania: \n 1. Adb i Fastboot poprawnie zainstalowane \n 2. Plik twrp.img znajdujący się w katalogu ze skrptem \n 3. Python w wersji 3 \n 4. Odblokowany bootloader")

		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 8:
		 
		clear

		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 9:
		 
		clear

		input("wcisnij enter aby kontynuowac")
		menu()
    elif case == 0:
        exit()
	else:
		clear
		print("Wybierz poprawną opcję!\n")

		input("wcisnij enter aby kontynuowac")
		menu()



menu()
