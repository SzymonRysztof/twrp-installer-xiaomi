# X.E.T Beta v0.7
## Xiaomi Essential Tools

<center><img src="https://github.com/mezutelni/twrp-installer-xiaomi/blob/master/xet.png"/></center>

# PL


#### UWAGA ja jako autor nie jestem odpowiedzialny za ŻADNE szkody
#### wyrządzone przez w.w skrypt! Używasz go na własną odpowiedzialność!

Zestaw narzedzi dla telefonów Xiaomi napisany w Pytonie

## Wymagania
-Colorama (python -m easy_install colorama)

### Instalacja

1. Fastboot i ADB<br>
  a)Na Windowsie instalujemy fastboot i adb (np. https://forum.xda-developers.com/showthread.php?t=2588979)<br>
  b)Na linuxie instalujemy naszym package manegerem (np. apt)<br>
2. Instalujemy pythona 3.6<br>
3. Uruchamiamy skrypt<br>
  a)Na Windowsie dwu klik na main.py<br>
  b)Na Linuxie najpier raz nadajemy uprawnienia 'chmod +x main.py' a potem każdorazowo w terminalu  ./main.py<br>

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

# EN

#### DISCLAIMER
#### I'm not responsible for bricked phones or dead sdcard! You do so at your own risk!

Essential toolkit for Xiaomi's phones coded in Python

## Requirements
-Colorama (python -m easy_install colorama)

### Installation

1. Fastboot & ADB<br>
  a)On Windows we have to install adb and fastboot (eg. https://forum.xda-developers.com/showthread.php?t=2588979)<br>
  b)On Linux we have to use our package manager (eg. apt)<br>
2. Install python 3.6<br>
3. Run script<br>
  a)On Windows double click main.py<br>
  b)On linux, first we have to give perrmissions to script once: 'chmod +x main.py' then start script from terminal  ./main.py<br>

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
