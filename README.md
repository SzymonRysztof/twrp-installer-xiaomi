# twrp-installer-xiaomi wersja beta 0.1

--------------------------------------------------------------------
UWAGA ja jako autor nie jestem odpowiedzialny za ŻADNE szkody
wyrządzone przez w.w skrypt! Używasz go na własną odpowiedzialność!
--------------------------------------------------------------------

Zautomatyzowany instalator TWRP dla wszystkich urządzeń Xiaomi z odblokowanym bootloaderem napisany w Pythonie

Wymagany python 3 do działania!

## Instrukcja Instalacji

1.Pobierz TWRP dla twojego telefonu ze strony https://twrp.me/Devices/ (Żeby poznać nazwe kodową urządzenia użyj aplikacji AIDA64 na telefonie)<br>
2.Zmien nazwe pliku na "twrp.img" i umieść go w tym samym katalogu co skrypt twrp_install.py<br>
3.Włącz debugowanie na telefonie<br>
4.Uruchom skrypt:<br>
 a)Na linuxie najpierw trzeba nadać flage wykonywania 'chmod +x twrp_install.py'
   a następnie uruchomić jak każdy skrypt z terminala './twrp_install.py'<br>
 b)Windows chwilowo jest NIE wspierany, obsługa tego OS to mój następny cel więc Stay Tuned ;) <br>
5.Wprowadź telefon w fastboot mode (można zrobić to z menu skryptu)

### Co potrafię:
-Potrafię zainstalować recovery na urządzeniach xiaomi z poziomu systemu linux<br>
-Potrafię zresetować telefon w trybach: System, Recovery, Fastboot<br>
-Określić stan odblokowania Bootloadera
