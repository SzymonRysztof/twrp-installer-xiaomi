# X.E.T Beta v0.2
## Xiaomi Essential Tools

<center><img src="https://github.com/mezutelni/twrp-installer-xiaomi/blob/master/xet.png"/></center>

# PL


#### UWAGA ja jako autor nie jestem odpowiedzialny za ŻADNE szkody
#### wyrządzone przez w.w skrypt! Używasz go na własną odpowiedzialność!

Zestaw narzedzi dla telefonów Xiaomi napisany w Pytonie

Wymagany python 3 do działania
dodatkowo na windowsie potrzebujemy zainstalować "adb and fastboot 15s installer"

## Instrukcja Instalacji

1.Pobierz TWRP dla twojego telefonu ze strony https://twrp.me/Devices/ (Żeby poznać nazwe kodową urządzenia użyj aplikacji AIDA64 na telefonie)<br>
2.Zmien nazwe pliku na "twrp.img" i umieść go w tym samym katalogu co skrypt twrp_install.py<br>
3.Włącz debugowanie na telefonie<br>
4.Uruchom skrypt:<br>
 a)Na linuxie najpierw trzeba nadać flage wykonywania 'chmod +x \*.py'
   a następnie uruchomić jak każdy skrypt z terminala './main.py'<br>
 b)Wystarczy kliknać dwa razy na main.py <br>
ps. Telefon powinien być w trybie fastboot jeśli chcesz instalować recvoery (Można go uruchomić z poziomu skryptu)<br>

### Co potrafię:
-Potrafię zainstalować recovery na urządzeniach xiaomi z poziomu systemu linux<br>
-Potrafię zresetować telefon w trybach: System, Recovery, Fastboot<br>
-Potrafię Określić stan odblokowania Bootloadera<br>
-Potrafię zmienić DPI<br>
-Potrafię zainstalować aplikację kamery z mi mix 2<br>
-Potrafię odblokować opcje zmiany siatki aplikacji aż do 10x10<br>
-Potrafię aktywować camera 2 api<br>

# EN

#### DISCLAIMER
#### I'm not responsible for bricked phones or dead sdcard! You do so at your own risk!

Essential toolkit for Xiaomi's phones coded in Python

Python 3+ is required
and for windows you will also need "adb and fastboot 15s installer"

## Install

1.Download TWRP for yout phone from https://twrp.me/Devices/ <br>
2.Change file name to twrp.img (eg. TWRP-3.1.1.0-CAPRICORN.img to twrp.img) <br>
3.Turn on USB debugging <br>
4.Start script <br>
  a)If you are on linux you have to add x flag to file 'chmod +x \*.py'<br>
    and then just start it like every script './main.py'<br>
  b)Just double click main.py <br>
ps. Phone have to be in fastboot mode for recovery install (You can use reboot menu in script)

### What Can i do:
-I can install recovery for you<br>
-I can reboot your phone to recovery, fastboot or system<br>
-I can tell if your bootloader is unlocked or not<br>
-I can change your dpi<br>
-I can install mi mix 2 camera app<br>
-I can allow you to change your desktop grid up to 10x10<br>
-I can activate camer 2 api<br>
