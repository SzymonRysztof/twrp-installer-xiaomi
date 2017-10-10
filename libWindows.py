import os
from sys import platform
import time
clear = lambda: os.system('cls')
def chckfl():
    f = os.path.isfile('fastboot.exe')
    a = os.path.isfile('adb.exe')
    if f == True and a == True:
        return True
    elif f == True and a == False:
        clear()
        print ("Nie znaleziono pliku binarnego adb w '/usr/bin'")
        print ("Nie można dokończyć działania programu!")
        exit()
    elif f == False and a == True:
        clear()
        print ("Nie znaleziono pliku binarnego Fastboot w '/usr/bin'")
        print ("Nie można dokończyć działania programu!")
        exit()
    elif f == False and a == False:
        clear()
        print ("Nie znaleziono plików binarnych Fastboot i Adb w '/usr/bin'")
        print ("Nie można dokończyć działania programu!")
        exit()
    else:
        clear()
        print ("Nieznany błąd! kończe działanie programu!")
        exit()
def installWin():
    chckfl()
    clear()
    twrpE = os.path.isfile('twrp.img')
    if twrpE == True:
        clear()
        os.system('fastboot devices')
        print ("Czy widzisz tutaj swój telefon (t/n): \n")
        deviceVisible = input('');
        deviceVisible = deviceVisible.lower()
        if deviceVisible == "n":
            clear()
            print()
            print ("Sprawdź połączenie telefonu z komputerem")
            print ("Telefon powinien wyświetlać króliczka (MiTu) grzebiącego w Androidowym Robocie")
            print ("Następnie uruchom ten program ponownie")
            print()
            exit()
        elif deviceVisible == "t":
            clear()
            print ("Świetnie, możemy przejść do następnego etapu!\n")
        else:
            clear()
            print ("Musisz wybrać opcję (T)ak albo (N)ie!")
            print()
            installWin()
        os.system('fastboot boot twrp.img')
        clear()
        print ("\nCzy na twoim telefonie pojawiło się TWRP (W zależności od telefonu może to trwać chwilę)? (t/n)")
        twrpS = input().lower()
        if twrpS == "n":
            clear()
            print ("Upewnij się że: \n 1.Posiadasz plik twrp.img (bez dodatkowych rozszerzeń!) \n 2.Twrp jest odpowiednie dobrane do twojego telefonu \n 3.Posiadasz odpowiednią wersję pythona \n ")
            print()
            exit()
        elif twrpS == "t":
            os.system('adb reboot bootloader')
            os.system('fastboot flash recovery twrp.img')
            os.system('fastboot boot twrp.img')
            print ("Proszę czekać cierpliwie, ok 10 sek")
            time.sleep(10)
            os.system('adb reboot recovery')
    else:
        clear()
        print ("Nie masz pliku twrp.img, pobierz go i umieść w folderze ze skryptem")
        print ()
        print ("https://twrp.me/Devices/")
        print ()
        exit()
    clear()
    print ("Gratualcję! Możesz cieszyć się zainstalowanym TWRP")
    i = 5;
    print ("Nastąpi powrót do menu głownego za: ")
    while (i>0):
        print (i)
        i=i-1
        time.sleep(1)
    exit()
