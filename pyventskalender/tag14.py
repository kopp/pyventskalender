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

# %%
# Diese Bilder finden sich unter
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Lade die Datei herunter und speichere Sie hier in dem Ordner mit dem Namen
# `galgenmannbilder.py`.

# %%
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

# Schreibe jetzt eine Funktion `galgenmannbild`, die als Parameter die Anzahl
# an Fehlern entgegennimmt und das Bild zurückliefert das der Anzahl an Fehlern
# entspricht.

def galgenmannbild(anzahl_fehler: int) -> str:
    return HANGMANPICS[anzahl_fehler]
# %%
