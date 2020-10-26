# Die Idee

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