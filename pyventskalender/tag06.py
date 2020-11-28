# Neben den einfachen Datenstrukturen, die wir bisher verwendet haben (`int`,
# `str`, `float`, `bool`), gibt es auch komplexere, zusammengesetzte
# Strukturen.
# Heute wollen wir uns die Liste, `list`, anschauen.
# Sie ist ein Beispiel für einen Container, also ein Objekt, das viele weitere
# Objekte enthält.

from typing import List

# %%
# Einerseits die Liste `list`, die mehrere Objekte enthalten kann.
# Geschrieben wird die Liste mit `[]`-Klammern:

meine_liebsten_tiere = ["Hase", "Frosch", "Ente"]

# Man kann sich eine Liste vorstellen wie 
# Eine Liste kann man sich vorstellen wie ein Regalbrett für Bücher.
#   - Die Bücher (Objekte) sind einer bestimmten Reihenfolge (und zwar in der, wie der Nutzer sie eingeräumt hat)
#   - Es können ganz verschiedene Bücher nebeneinander stehen (eine Liste kann Objekte von verschiedene Typen enthalten)
#   - Man kann einzelne Bücher aus dem Regal nehmen und neue Bücher zwischen bereits vorhandene stellen


# %%
# Mit Listen kann man verschiedene Dinge machen, beispielsweise abfragen, wie
# lang sie sind

len(meine_liebsten_tiere)

# %%
# Oder prüfen, ob ein bestimmtes Element darin enthalten ist

"Katze" in meine_liebsten_tiere

# %%
# Dann auch Elemente hinzufügen

meine_liebsten_tiere.append("Katze")

# (Jetzt könnte man wieder testen, ob "Katze" in der Liste enhalten ist...)

# %%
# Oder Elemente entfernen

meine_liebsten_tiere.remove("Ente")
# %%
# Die Elemente in einer Liste können übrigens verschiedene Typen haben -- bspw.

stuff = [1, "zwo", 3, "und", ["eine", "Liste in der", "Liste"]]

# %% Liste anlegen -- Test 10
# Erstelle jetzt bitte eine Leere Liste mit Namen `unverstanden`

# %% Lieblingstiere erfragen -- Tests 20 30
# Vervollständige jetzt die folgende Funktion.
# Sie soll den Nutzer nach seinen Lieblingstieren fragen und eine Liste von 3
# verschiedenen Tieren ausgeben.
# Gibt der Nutzer zwei mal das gleiche Tier ein, soll er nochmal gefragt werden.
# Ein Aufruf der Funktion mit Interaktion des Nutzers könnte so aussehen:
#     Nenne ein Lieblingstier:
#     > Igel
#     Nenne ein Lieblingstier:
#     > Katze
#     Nenne ein Lieblingstier:
#     > Katze
#     Katze hattest du schon gesagt.
#     Nenne ein Lieblingstier:
#     > Frosch
# Dann müsste die Ausgabe
#     ["Igel", "Katze", "Frosch"]
# sein.
#
# Übrigens: Die Funktion `input("Frage")` Fragt den Nutzer mit dem Text "Frage"
# nach einer Eingabe und gibt als Ergebnis diese Eingabe zurück.

def frage_nach_lieblingstieren() -> List[str]:
    pass

# %% Lieblingstiere -- Test 40
# Auf die einzelnen Elemente einer Liste kann man per Index zugreifen.
# Das erste Element hat den Index 0, das zweite 1, usw.
# Eine Liste mit n Elementen hat also Indices 0, 1, ..., n-1.
#
# Implementiere damit eine Funktion, die
# - als eingabe eine Liste mit 3 Tieren bekommt -- das sind die gekürten Lieblingstiere (Platz 1, Platz 2, Platz 3)
# - und ein einzelnes Tier
# Sie soll den Platz ausgeben, den das einzelne Tier in der Liste der Gewinner
# inne hat.
# Ist das Tier nicht enthalten, soll dei Funktion `None` zurück geben.
# Also bspw.
#    ["Hund", "Katze", "Maus"], "Katze"  -->  2  (weil 2. Platz)
#    ["Hund", "Katze", "Maus"], "Elch"   -->  None

def platz_auf_siegertreppchen(siegertiere: List[str], einzelnes_tier: str):
    pass