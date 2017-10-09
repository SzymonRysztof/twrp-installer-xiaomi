#!/usr/bin/python3
import os
from sys import platform
import time



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
		print ("Czy widzisz tutaj swój telefon (t/n): ")
		deviceVisible = input('');
		deviceVisible = deviceVisible.lower()

		if deviceVisible == "n":
			print ("Sprawdź połączenie telefonu z komputerem")
			print ("Telefon powinien wyświetlać króliczka (MiTu) grzebiącego w Androidowym Robocie")
			#tutaj wstawić powrót do początku

			exit()
		elif deviceVisible == "t":
			print ("Świetnie, możemy przejść do następnego etapu!\n")
		else:
			print ("Musisz wybrać opcję (T)ak albo (N)ie!")
			#tutaj wstawić powrót do początku

			exit()

		os.system('fastboot boot twrp.img')
		print ("\n Czy na twoim telefonie pojawiło się TWRP(W zależności od telefonu może to trwać chwilę)? (t/n)")
		twrpS = input().lower()

		if twrpS == "n":
			print ("Upewnij się że: \n 1.Posiadasz plik twrp.img (bez dodatkowych rozszerzeń!) \n 2.Twrp jest odpowiednie dobrane do twojego telefonu \n 3.Posiadasz odpowiednią wersję pythona \n ")

			#tutaj wstawić powrót do początku
			exit()

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
		return (1)

		#tutaj wstawić powrót do początku
		exit()

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
	print ("Witaj, ten prosty skrypt przeprowadzi Cię przez proces instalacji Recovery na twoim telefonie XIAOMI")
	print ("1. Instaluj Recovery")
	print ("2. Zrebootuj do Recovery")
	print ("3. Zrebootuj do Fastboot")
	print ("4. Wymagania")
	print ("5. O Autorze")
	print ("6. Kontakt")
	case = int(input())
	if case == 1:
		start()
	elif case == 2:
		os.system('adb reboot recovery')
	elif case == 3:
		os.system('adb reboot fastboot')
	elif case == 4:
		print("Wymagania: \n 1. Adb i Fastboot poprawnie zainstalowane \n 2. Plik twrp.img znajdujący się w katalogu ze skrptem \n 3. Python w wersji 3 \n 4. Odblokowany bootloader")
	elif case == 5:
		print("")
	elif case == 6:
		print("")
	else:
		os.system("cls")
		os.system("clear")
		print("Wybierz poprawną opcję!\n")

		menu()

os.system('cls')
os.system('clear')

menu()
