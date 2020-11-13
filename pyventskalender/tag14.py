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
# Du kannst sie testen per bspw. `print(galgenmannbild(3))`


def galgenmannbild(anzahl_fehler: int) -> str:
    return HANGMANPICS[anzahl_fehler]

# %%


MAXIMAL_ERLAUBTE_FEHLER = len(HANGMANPICS) - 1


def zeige_zu_ratendes_wort(gesuchtes_wort, fehlende_buchstaben):
    anzuzeigendes_wort = gesuchtes_wort
    for fehlender_buchstabe in fehlende_buchstaben:
        anzuzeigendes_wort = anzuzeigendes_wort.replace(fehlender_buchstabe, "_")
    print("Gesucht: {}".format(anzuzeigendes_wort))


def ist_buchstabe(eingabe_von_nutzer):
    if len(eingabe_von_nutzer) != 1:
        print("Bitte genau einen Buchstaben angeben")
        return False
    return True


def ist_aufgeben(eingabe_von_nutzer):
    return eingabe_von_nutzer.lower() == "aufgeben"


def galgenmannspiel(gesuchtes_wort: str):
    gesuchtes_wort = gesuchtes_wort.strip()
    anzahl_fehler = 0
    noch_gesuchte_buchstaben = set(gesuchtes_wort.lower())
    falsch_geratene_buchstaben = []
    while anzahl_fehler < MAXIMAL_ERLAUBTE_FEHLER:
        zeige_zu_ratendes_wort(gesuchtes_wort, noch_gesuchte_buchstaben)
        eingabe = input("Rate einen Buchstaben")
        if ist_aufgeben(eingabe):
            break
        if not ist_buchstabe(eingabe):
            continue
        buchstabe = eingabe.strip().lower()
        if buchstabe in noch_gesuchte_buchstaben:
            noch_gesuchte_buchstaben.remove(buchstabe)
            if len(noch_gesuchte_buchstaben) == 0:
                print("Erraten!  Das Wort war {}".format(gesuchtes_wort))
                return
        else:
            falsch_geratene_buchstaben.append(buchstabe)
            anzahl_fehler += 1
            print("{} ist leider falsch; bisher falsch geraten: {}".format(
                buchstabe,
                falsch_geratene_buchstaben))
            print(galgenmannbild(anzahl_fehler))
    print("Leider nicht geklappt -- das Wort war {}".format(gesuchtes_wort))


# %%
