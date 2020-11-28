# PyVentskalender -- Die Idee

Jeden Tag gibt es eine (hoffentlich) einfache Aufgabe in Python, die gelöst
werden muss.
Dazu kommt jeden Tag in den Ordner `pyventskalender` eine neue Datei.
Sie enthält eine Beschreibung, was zu tun ist.

Die aktuellen Probleme bekommt man, indem man

    python gib_mir_die_heutige_aufgabe.py

Um zu schauen, ob man die Aufgabe erfüllt hat, lässt man einfach

    python ich_will_meine_belohnung.py

laufen.
Wenn man fertig ist, wird hier die Belohnung des Tages angezeigt.
Wenn man noch nicht fertig ist, dann werden hier die Probleme angezeigt, die
man noch lösen muss.

Die Probleme werden übrigens anhand von
[Unit Tests](https://www.it-agile.de/wissen/agiles-engineering/unit-tests/)
aufgedeckt.
Diese sind -- für interessierte -- im Ordner `test` zu finden.

Implementiert sind sie mit
[`unittest`](https://docs.python.org/3/library/unittest.html)
und damit kann man sie auch ausführen, indem man hier

    python -m unittest

eingibt.


# Den PyVentskalender einrichten

## Grundlagen

- Python muss installiert sein, sodass man es in der Kommandozeile direkt aufrufen kann (also `python` eintippen muss reichen).
  - Unter Windows ist die
    [Installation per Microsoft Store](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7)
    empfohlen.
  - Unter Linux ist die Installation aus Paketquellen empfohlen
    (Ubuntu: `sudo apt install python3`, Arch Linux: `sudo pacman -S python`, ...)
  - Unter Mac OS ist die Installation per Brew `brew install python3` empfohlen.
- [Visual Studio Code](https://code.visualstudio.com/) muss installiert sein.
- Das
  [Python Plugin für Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  muss in Visual Studio Code installiert sein.

## Den PyVentskalender selbst "installieren"

Es reicht, die Datei
[`gib_mir_die_heutige_aufgabe.py`](https://raw.githubusercontent.com/kopp/pyventskalender/master/gib_mir_die_heutige_aufgabe.py)
in einen bisher leeren Ordner zu legen, dann kann man direkt loslegen.
Wenn die Datei ausgeführt wird, lädt sie automatisch alles weitere herunter.

Es gibt eine Konfigurationsdatei für den Kalender.
Hier können bspw. die Belohnungen, die man bekommen kann, festgelegt werden.
Standardmäßig wird die Datei
[`pyventskalender.default-config.json`](pyventskalender.default-config.json)
heruntergeladen.
Um eine eigene Konfiguration zu hinterlegen, sollte diese Datei angepasst werden und unter den Namen
[`pyventskalender.config.json`](pyventskalender.config.json)
gespeichert werden.
