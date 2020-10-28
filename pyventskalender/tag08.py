# Noch sinnvoller kann man mit der `for`-Schleife arbeiten, wenn man damit Code
# für die einzelnen Elemente einer Collection -- bspw. einer `list` ausführt.


# %%
# Damit kann man beispielsweise sagen, dass man die folgenden Tiere mag:

tiere = ["Hunde", "Katzen", "Maulwürfe"]
def ich_mag(tiere):
    for tier in tiere:
        print("Ich mag {}".format(tier))


# %%
# Vervollständige jetzt die Funktion, die aus einer Liste alle Säugetiere
# heraussucht.
# Alle bekannten Säugetiere sind in 

BEKANNTE_SAEUGETIERE = [
    "Hund",
    "Katze",
    "Affe",
    "Mensch",
    "Maulwurf",
    "Pferd",
]

# verfügbar.
# Beispielsweise sollte
#    saeugetiere_aus(["Hund", "Fisch", "Eidechse", "Affe"])
# das folgende Ergebnis liefern:
#    ["Hund", "Affe"]

from typing import List

def saeugetiere_aus(tiere: List[str]) -> List[str]:
    pass

# %%
# Viele Menschen mögen Tiere.
# Die folgende Funktion soll alle Kombinationen zwischen Mensch und Tier finden
# und dann jeweils den Satz
#    <mensch> mag <tier>
# in eine Liste schreiben und diese ausgeben.
# Sind bspw. die Menschen ["Peter", "Paul"] und die Tiere ["Schweine", "Katzen"] gegeben, dann sollte das Ergebnis sein
#    ["Peter mag Schweine", "Peter mag Katzen", "Paul mag Schweine",
#     "Paul mag Katzen"]
# Hinweis: Sortiert sollte nach Menschen sein.

def mensch_mag_tier(menschen: List[str], tiere: List[str]) -> List[str]:
    pass
