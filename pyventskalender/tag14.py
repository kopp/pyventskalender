# Heute wollen wir das Spiel "Galgenmännchen" spielen.

# Mit Bildern tun wir es uns gerade noch etwas schwer.
# Man kann aber einfache Bilder "zeichnen", indem man Buchstaben und Zeichen
# clever anordnet.
# Glücklicherweise hat das schon jemand für Galgenmännchen gemacht.
# Beispielsweise sieht der leere Galgen dann so aus:
#       +---+
#       |   |
#           |
#           |
#           |
#           |
#     =========
# und der volle so:
#       +---+
#       |   |
#       O   |
#      /|\  |
#      / \  |
#           |
#     =========

# %% Bilder herunterladen -- Tests 10 20
# Diese Bilder finden sich unter
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Lade die Datei herunter und speichere Sie hier in dem Ordner mit dem Namen
# `galgenmannbilder.py`.

# %% Bilder importieren -- Test 30
# Wenn das geschehen ist, dann kannst du die Bilder importieren per
try:
    from pyventskalender.galgenmannbilder import HANGMANPICS
# Das holt die Variable `HANGMANPICS` aus der Datei `galgenmannbilder.py` im
# Ordner `pyventskalender`.
# Leider gibt es hier noch ein Problem:
# Wenn der Code hier per _Run Cell_ in Visual Studio Code ausgeführt wird, dann
# "sieht" Visual Studio Code nicht, dass die Datei eigentlich im Ordner
# "pyventskalender" liegt und es gibt den Fehler `ImportError`.
# In diesem Fall laden wir die Datei direkt von "hier" (also Ohnen einen Ordner
# anzugeben):
except ImportError:
    from galgenmannbilder import HANGMANPICS


# %% Bild anzeigen -- Tests 40 50
# Schreibe jetzt eine Funktion `galgenmannbild`, die als Parameter die Anzahl
# an Fehlern entgegennimmt und das Bild zurückliefert das der Anzahl an Fehlern
# entspricht.
# Du kannst sie testen per bspw. `print(galgenmannbild(3))`


# def ...

# %% Maximale Fehler -- Tests 60 70
# Wie viele Fehler darf man sich denn eigentlich erlauben, wenn man diese
# Anzahl von Bildern zur Verfügung hat?
# Definiere eine Variable `VERLOREN_BEI_SO_VIELEN_FEHLERN` mit dem richtigen
# Wert.



# %% Unbekannte Buchstaben verbergen -- test 80
# Als letzte Übung für heute vervollständige bitte noch die folgende Funktion.
# Sie soll das gesuchte Wort (das der ratende ja nicht kennt) und die
# Buchstaben, die noch nicht erraten wurden, entgegen nehmen und das Wort
# zurückgeben, wobei alle noch zu erratenden Buchstaben durch ein `_` ersetzt
# sind.
# Ist also `hallo` zu erraten und `h` und `l` müssen noch erraten werden, dann
# soll die Ausgabe `_a__o` sein.

def zu_ratendes_wort(gesuchtes_wort, fehlende_buchstaben):
    pass


# %%
# Ok, das ist schon ziemlich gut.  Morgen mehr!