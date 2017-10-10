import os
from sys import platform
import time
from libWindows import bcolors
clear = lambda: os.system('clear')
def chckfl():
    f = os.path.isfile('/usr/bin/fastboot')
    a = os.path.isfile('/usr/bin/adb')
    if f == True and a == True:
        return True
    elif f == True and a == False:
        clear()
        print (bcolors.FAIL+"Nie znaleziono pliku binarnego adb w '/usr/bin'")
        print ("Nie można dokończyć działania programu!"+bcolor.ENDC)
        exit()
    elif f == False and a == True:
        clear()
        print (bcolors.FAIL+"Nie znaleziono pliku binarnego Fastboot w '/usr/bin'")
        print ("Nie można dokończyć działania programu!"+bcolor.ENDC)
        exit()
    elif f == False and a == False:
        clear()
        print (bcolors.FAIL+"Nie znaleziono plików binarnych Fastboot i Adb w '/usr/bin'")
        print ("Nie można dokończyć działania programu!"+bcolor.ENDC)
        exit()
    else:
        clear()
        print (bcolors.FAIL+"Nieznany błąd! kończe działanie programu!"+bcolor.ENDC)
        exit()
def installLinux():
    chckfl()
    clear()
    twrpE = os.path.isfile('twrp.img')
    if twrpE == True:
        clear()
        os.system('fastboot devices')
        print (bcolors.OKBLUE+"Czy widzisz tutaj swój telefon (t/n): \n"+bcolors.ENDC)
        deviceVisible = input('');
        deviceVisible = deviceVisible.lower()
        if deviceVisible == "n":
            clear()
            print ("Sprawdź połączenie telefonu z komputerem")
            print ("Telefon powinien wyświetlać króliczka (MiTu) grzebiącego w Androidowym Robocie")
            print ("Następnie uruchom ten program ponownie")
            exit()
        elif deviceVisible == "t":
            clear()
            print (bcolors.OKGREEN+"Świetnie, możemy przejść do następnego etapu!\n"+bcolors.ENDC)
        else:
            clear()
            print (bcolors.FAIL+"Musisz wybrać opcję (T)ak albo (N)ie!"+bcolors.ENDC)
            installLinux()
        os.system('fastboot boot twrp.img')
        clear()
        print (bcolors.OKBLUE+"\nCzy na twoim telefonie pojawiło się TWRP (W zależności od telefonu może to trwać chwilę)? (t/n)"+bcolors.ENDC)
        twrpS = input().lower()
        if twrpS == "n":
            clear()
            print ("Upewnij się że: \n 1.Posiadasz plik twrp.img (bez dodatkowych rozszerzeń!) \n 2.Twrp jest odpowiednie dobrane do twojego telefonu \n 3.Posiadasz odpowiednią wersję pythona \n ")
            exit()
        elif twrpS == "t":
            os.system('adb reboot bootloader')
            os.system('fastboot flash recovery twrp.img')
            os.system('fastboot boot twrp.img')
            print (bcolors.OKBLUE+"Proszę czekać cierpliwie, ok 10 sek"+bcolors.ENDC)
            time.sleep(10)
            os.system('adb reboot recovery')
    else:
        clear()
        print (bcolors.FAIL+"Nie masz pliku twrp.img, pobierz go i umieść w folderze ze skryptem\n"+bcolors.ENDC)
        print ("https://twrp.me/Devices/")
        exit()
    clear()
    print (bcolors.OKGREEN+"Gratualcję! Możesz cieszyć się zainstalowanym TWRP"+bcolors.ENDC)
    i = 5;
    print ("Nastąpi powrót do menu głownego za: ")
    while (i>0):
        print (i)
        i=i-1
        time.sleep(1)
    os.system('./main.py')
