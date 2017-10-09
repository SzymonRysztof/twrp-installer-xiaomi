#!/usr/bin/python3
import os
from sys import platform
import time


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
		return False
	elif f == False and a == True:
		print ("Nie znaleziono pliku binarnego Fastboot w '/usr/bin'")
		return False
	elif f == False and a == False:
		print ("Nie znaleziono plików binarnych Fastboot i Adb w '/usr/bin'")
		return False
	else:
		print ("Nieznany błąd! kończe działanie programu!")
		menu()
#ta funkcja sprawdza czy zainstalowany jest fastboot w windowsie
"""def chckfw():
	f = os.path.isfile('/usr/bin/fastboot')
	a = os.path.isfile('/usr/bin/adb')
	if f == True and a == True:
		return True
	elif f == True and a == False:
		print ("Nie znaleziono pliku binarnego adb w '/usr/bin'")
		return False
	elif f == False and a == True:
		print ("Nie znaleziono pliku binarnego Fastboot w '/usr/bin'")
		return False
	elif f == False and a == False:
		print ("Nie znaleziono plików binarnych Fastboot i Adb w '/usr/bin'")
		return False
	else:
		print ("Nieznany błąd! kończe działanie programu!")
		exit ()
"""
#Ta funckja odpowiada za proces instalacji na linuxie
def installLinux():

	os.system('clear')
	print ()
	print ()
	print ()
	deviceVisible = "n"
	twrpE = os.path.isfile('twrp.img')
	if twrpE == True:

		os.system('fastboot devices')
		print ("Czy widzisz tutaj swój telefon (t/n): \n")
		deviceVisible = input('');
		deviceVisible = deviceVisible.lower()

		if deviceVisible == "n":
			print()
			print ("Sprawdź połączenie telefonu z komputerem")
			print ("Telefon powinien wyświetlać króliczka (MiTu) grzebiącego w Androidowym Robocie")
			print()
			menu()
		elif deviceVisible == "t":
			print ("Świetnie, możemy przejść do następnego etapu!\n")
		else:
			print ("Musisz wybrać opcję (T)ak albo (N)ie!")
			print()

			menu()

		os.system('fastboot boot twrp.img')
		print ("\n Czy na twoim telefonie pojawiło się TWRP(W zależności od telefonu może to trwać chwilę)? (t/n)")
		twrpS = input().lower()

		if twrpS == "n":
			print ("Upewnij się że: \n 1.Posiadasz plik twrp.img (bez dodatkowych rozszerzeń!) \n 2.Twrp jest odpowiednie dobrane do twojego telefonu \n 3.Posiadasz odpowiednią wersję pythona \n ")
			print()

			menu()

		elif twrpS == "t":

			os.system('adb reboot bootloader')
			os.system('fastboot flash recovery twrp.img')
			os.system('fastboot boot twrp.img')
			time.sleep(10)
			os.system('adb reboot recovery')



	else:
		print ("Nie masz pliku twrp.img, pobierz go i umieść w folderze ze skryptem")
		print ()
		print ("https://twrp.me/Devices/")
		print ()
		menu()

	os.system('clear')
	print ("Gratualcję! Możesz cieszyć się zainstalowanym TWRP")
	exit()

def start():

	if platform == "linux" or platform == "linux2":
		sys = "l"

	elif platfrom == "win32":
		sys = "w"
	else:
		Print ("Przykro mi, na chwilę obecną wspierane systemy to: Windows i Linux")

	os.system('cls')
	os.system('clear')
	if sys == "l":
		chckfl()
		if chckfl() is True:
			installLinux()
		elif chckfl() is False:
			menu()
	"""
	elif sys =="w":
		chckfw()
		if chckfw() is True:
			installWindows()
		elif chckfw() is False:
			menu()
	"""




#Menu głowne programu!
def menu():
	os.system('cls')
	os.system('clear')
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
	case = int(input("Wybierz: "))
	if case == 1:
		start()
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
		os.system('cls')
		os.system('clear')
		print ("--------------------------------------------------------------------------------------------------------")
		print ("Status odblokowanie twojego bootloader to:                                                              ")
		bl()
		print ("--------------------------------------------------------------------------------------------------------")

		input("wcisnij enter aby kontynuowac")
		menu()

	elif case == 7:
		os.system('cls')
		os.system('clear')
		print("Wymagania: \n 1. Adb i Fastboot poprawnie zainstalowane \n 2. Plik twrp.img znajdujący się w katalogu ze skrptem \n 3. Python w wersji 3 \n 4. Odblokowany bootloader")

		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 8:
		os.system('cls')
		os.system('clear')

		input("wcisnij enter aby kontynuowac")
		menu()
	elif case == 9:
		os.system('cls')
		os.system('clear')

		input("wcisnij enter aby kontynuowac")
		menu()

	else:
		os.system("cls")
		os.system("clear")
		print("Wybierz poprawną opcję!\n")

		input("wcisnij enter aby kontynuowac")
		menu()



menu()
