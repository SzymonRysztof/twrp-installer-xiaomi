# X.E.T Beta v0.7
## Xiaomi Essential Tools

<center><img src="https://github.com/mezutelni/twrp-installer-xiaomi/blob/master/xet.png"/></center>

# PL


#### UWAGA ja jako autor nie jestem odpowiedzialny za ŻADNE szkody
#### wyrządzone przez w.w skrypt! Używasz go na własną odpowiedzialność!

Zestaw narzedzi dla telefonów Xiaomi napisany w Pytonie

## Wymagania
- Python
- Colorama

### Instalacja
Windows:<br>
    1. Instalujemy pythona w wersji 3.X<br>
    2. Instalujemy moduł colorama dla pythona:<br>
       - Znajdujemy lokalizacje pythona (domyślnie c:\Users\$user\AppData\Local\Programs\PythonX\)<br>
       - Otwieramy te lokalizację w cmd<br>
       - wpisujemy "Scripts\pip.exe install colorama"<br>
    3. Pobieramy i instalujemy ADB + Fastboot (Ważne jest żeby znajdowały się w PATH systemowych!)<br>
    4. Pobieramy repozytprium z GitHub<br>
    5. Uruchamiamy XET.py<br>
Linux:<br>
    Instrukcja dla ubuntu i mu podobnych, ale zasada ta sama dla każdej dystrybucji<br>
    1. `sudo apt-get install python3 python-pip git android-tools-adb android-tools-fastboot`<br>
    2. `sudo pip-install colorama`<br>
    3. `git clone https://github.com/mezutelni/twrp-installer-xiaomi.git`<br>
    4. Otwieramy terminal w miejscu lokalizacji pliku<br>
    5. `chmod +x XET.py`<br>
    6. Uruchamiamy z terminala przez `./XET.py`<br>

### Funkcje:
- Instalacja recovery dla odblokowanych urządzeń<br>
- Resetowanie telefonu do trybu fastboot, recovery, sideload, system<br>
- Bootowanie TWRP z pliku (przydatne dla osób które nie chcą instalować TWRP, np. na globalu)<br>
- Określanie stanu bootloader (odblokowany/zablokowany)<br>
- Sideloadowanie paczek zip (drag and drop)<br>
#### Tweaki systemowe:
- Tworzenie i przywracanie backupu build.prop<br>
- Zmiana DPI<br>
- Instalacja aplikacji kamery z Mi Mix 2(Automatyczny backup starej aplikacji w /system/priv-app/MiuiCamera/MiuiCamera.bak)<br>
- Odblokowanie opcji zmiany siatki pulpitu aż do 10x10 (Automatyczny backup starego pliku do /system/media/themes/default/com.miui.home.old)<br>
- Aktywacja camera 2 api<br>
- Usuwanie aplikacji systemowych<br>

# EN

#### DISCLAIMER
#### I'm not responsible for bricked phones or dead sdcard! You do so at your own risk!

Essential toolkit for Xiaomi's phones coded in Python

## Requirements
- Python
- Colorama (python module)


### Installation

Windows:<br>
    1. Install python 3<br>
    2. Install colorama for python:<br>
       - Find python.exe location (default c:\Users\$user\AppData\Local\Programs\PythonX\)<br>
       - Open it in cmd<br>
       - Type "Scripts\pip.exe install colorama"<br>
    3. Download and install ADB + Fastboot (Its your choice, but make sure that they are in PATH)<br>
    4. Download repo from GitHub<br>
    5. Run XET.py (The best way is to open it in CMD so you can send me crash notes)<br>
Linux:<br>
    For ubuntu family:<br>
    1. `sudo apt-get install python3 python-pip git android-tools-adb android-tools-fastboot`<br>
    2. `sudo pip-install colorama`<br>
    3. `git clone https://github.com/mezutelni/twrp-installer-xiaomi.git`<br>
    4. Open terminal in repo location<br>
    5. `chmod +x XET.py`<br>
    6. Run `./XET.py` in terminal<br>


### Functions:
- Installing twrp for unlocked phones<br>
- Rebooting phone to fastboot, recovery, sideload, system<br>
- Booting twrp directly from file (Usefull if you don't want to install recovery, eg. when you are using global)<br>
- Checking bootloader status (locked/unlocked)<br>
- Sideloading zips (drag and drop)<br>
#### System tweaks:
- Backing up and restoring build.prop file<br>
- Changing DPI<br>
- Installing Mi Mix 2 camera apk (Auto backup old file to /system/priv-app/MiuiCamera/MiuiCamera.bak)<br>
- Installing custom grid size up to 10x10 (Auto backup old file to /system/media/themes/default/com.miui.home.old)<br>
- Camera 2 API activation<br>
- Removing system Apps<br>