def installLinux():
    chckfl()
	clear
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

	clear
	print ("Gratualcję! Możesz cieszyć się zainstalowanym TWRP")
	exit()


	"""if sys == "l":
		chckfl()
		if chckfl() is True:
			installLinux()
		elif chckfl() is False:
			menu()
            """