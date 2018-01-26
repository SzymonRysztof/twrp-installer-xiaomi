# X.E.T Beta v0.7
## Xiaomi Essential Tools

<center><img src="https://github.com/mezutelni/twrp-installer-xiaomi/blob/master/xet.png"/></center>

# PL


#### UWAGA ja jako autor nie jestem odpowiedzialny za ŻADNE szkody
#### wyrządzone przez w.w skrypt! Używasz go na własną odpowiedzialność!

Zestaw narzedzi dla telefonów Xiaomi napisany w Pytonie

## Wymagania
-Python
-Colorama

### Instalacja
Windows:
    1.Instalujemy pythona w wersji 3.
    2.Instalujemy moduł colorama dla pythona:
        Znajdujemy lokalizacje pythona (domyślnie c:\Users\$user\AppData\Local\Programs\PythonX\)
        Otwieramy te lokalizację w cmd
        wpisujemy "Scripts\pip.exe install colorama"
    3.Pobieramy i instalujemy ADB + Fastboot (Ważne jest żeby znajdowały się w PATH systemowych!)
    4.Pobieramy repozytprium z GitHub
    5.Uruchamiamy XET.py (najlepiej otworzyć cmd, przeciągnąć xet.py i kliknąć enter, w razie błedu okno się nie zamknie i będziecie mogli wysłać mi screenshoot)
Linux:
    Instrukcja dla ubuntu i mu podobnych, ale zasada ta sama dla każdej dystrybucji
    1.sudo apt-get install python3 python-pip git android-tools-adb android-tools-fastboot
    2.sudo pip-install colorama
    3.git clone https://github.com/mezutelni/twrp-installer-xiaomi.git
    4.Otwieramy terminal w miejscu lokalizacji pliku
    5.chmod +x XET.py
    6.Uruchamiamy z terminala przez ./XET.py

### Funkcje:
-Pobieranie i instalacja recovery dla wspieranych urządzeń (oficjalne twrp)<br>
-Resetowanie telefonu do trybu fastboot, recovery, sideload, system<br>
-Określanie stanu bootloader (odblokowany/zablokowany)<br>
-Sideloadowanie paczek zip (drag and drop)<br>
#### Tweaki systemowe:
-Tworzenie i przywracanie backupu build.prop<br>
-Zmiana DPI<br>
-Instalacja aplikacji kamery z Mi Mix 2(Automatyczny backup starej aplikacji w /system/priv-app/MiuiCamera/MiuiCamera.bak)<br>
-Odblokowanie opcji zmiany siatki pulpitu aż do 10x10 (Automatyczny backup starego pliku do /system/media/themes/default/com.miui.home.old)<br>
-Aktywacja camera 2 api<br>
-Usuwanie aplikacji systemowych<br>

# EN

#### DISCLAIMER
#### I'm not responsible for bricked phones or dead sdcard! You do so at your own risk!

Essential toolkit for Xiaomi's phones coded in Python

## Requirements
-Python
-Colorama


### Installation

Windows:
    1.Install python 3
    2.Install colorama for python:
        Find python.exe location (default c:\Users\$user\AppData\Local\Programs\PythonX\)
        Open it in cmd
        Type "Scripts\pip.exe install colorama"
    3.Download and install ADB + Fastboot (Its your choice, but make sure that they are in PATH)
    4.Download repo from GitHub
    5.Run XET.py (The best way is to open it in CMD so you can send me crash notes)
Linux:
    For ubuntu family:
    1.sudo apt-get install python3 python-pip git android-tools-adb android-tools-fastboot
    2.sudo pip-install colorama
    3.git clone https://github.com/mezutelni/twrp-installer-xiaomi.git
    4.Open terminal in repo location
    5.chmod +x XET.py
    6.Run ./XET.py in terminal


### Functions:
-Downloading and installing twrp for supported phones (this with official TWRP)<br>
-Rebooting phone to fastboot, recovery, sideload, system<br>
-Checking bootloader status (locked/unlocked)<br>
-Sideloading zips (drag and drop)<br>
#### System tweaks:
-Backing up and restoring build.prop file<br>
-Changing DPI<br>
-Installing Mi Mix 2 camera apk (Auto backup old file to /system/priv-app/MiuiCamera/MiuiCamera.bak)<br>
-Installing custom grid size up to 10x10 (Auto backup old file to /system/media/themes/default/com.miui.home.old)<br>
-Camera 2 API activation<br>
-Removing system Apps<br>