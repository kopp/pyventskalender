# Bedingungen (if/else) erlauben, bestimmten Code nur in bestimmten Fällen
# auszuführen.
# Schleifen (um die es heute gehen soll) erlauben es, den selben Code immer
# wieder auszuführen.
#
# Eine `while`-Schleife in Python führt den selben Code so lange aus,
# wie eine bestimmte Bedingung wahr ist.

# %%
# Der folgende Code fragt bspw. so lange nach, ob er dich richtig verstanden
# hat, bis du die "richtige" Antwort gibst.
# Probiere ihn aus per `magst_du("Katzen")`.

def magst_du(tiername: str) -> bool:
    antwort = "nein"
    while antwort != "ja":
        antwort = input("Magst du {} (ja/nein)".format(tiername))
    return "Super, du magst also {}".format(tiername)

# Die Bedingung hier ist, dass `antwort` verschieden ist von `ja` -- also
# sobald man etwas anderes eingibt, ist die Bedingung wahr und der Code in dem
# Block (hier der `input`-Befehl) wird ausgeführt.


# %%
# Ein beliebter Trick ist, eine `while True`-Schleife mit einer `if`-Abfrage zu
# kombinieren.
# `while True` läuft unendlich lang (weil die Bedingung `True` ja immer wahr
# ist).
# Um die Schlefe dann zu verlassen, kann man entweder `break` (das beendet die
# Schleife) oder `return` (das beendet die Funktion) verwenden.
#
# Die Funktion von oben könnte man damit auch so schreiben:

def magst_du_reloaded(tiername: str) -> bool:
    while True:
        antwort = input("Magst du {} (ja/nein)".format(tiername))
        if antwort == "ja":
            return "Super, du magst also {}".format(tiername)

# %% Ratespiel lösen -- Test 10
# Damit können wir das erste einfache Spiel nicht nur selbst spielen, sondern
# den Computer spielen lassen.
# Hier ist nochmal das Spiel:

import random
zufallszahl = random.randint(1, 20)

def ich_tippe_auf(zahl: int):
    if zahl > zufallszahl:
        return "falsch, zu hoch"
    elif zahl < zufallszahl:
        return "falsch, zu niedrig"
    else:
        return "richtig, gefunden!"

# Vervollständige jetzt die folgende Funktion, die die Zufallszahl finden soll.
# Die Funktion sollte so lange `ich_tippe_auf` ausführen, bis die korrekte Zahl
# gefunden ist und diese am Ende ausgeben.

def finde_zufallszahl():
    pass

# Achtung: Wenn man die Funktion `finde_zufallszahl` mehrmals ausführt, findet
# sie immer die selbe Zufallszahl, weil diese oben nur einmal bestimmt wird.
# Damit man mit verschiedenen Zahlen arbeiten kann, kann man die folgende
# Funktion aufrufen, um eine neue Zufallszahl zu bekommen:

def neue_zufallszahl():
    global zufallszahl
    zufallszahl = random.randint(1, 20)

# Das `global` ist notwendig, um globale Variablen (die nicht in einer Funktion definiert werden) modifizieren zu können.
# Ohne das `global` würde man in der Funktion eine Variable `zufallszahl`
# anlegen, die zwar genau so heißt, wie die Funktion, die wir modifizieren
# wollen, aber eben leider nicht die selbe Variable ist.

# %%
