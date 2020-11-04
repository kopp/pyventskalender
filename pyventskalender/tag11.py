# Heute geht es um das Dictionary, `dict`, einen Container, mit dem man Daten
# mit "Stichworten" ablegen und auslesen kann.
#
# Wir bleiben thematisch beim Einlesen der Datei mit Gewichten.
# Wie wir sie lesen und den Inhalt extrahieren haben wir verstanden.
# Doch um aktuell bspw. die Frage zu beantworten, was das Höchstgewicht von
# Caro im beobachteten Zeitraum war, muss man relativ viel Code schreiben.
#
# Schöner wäre es, wenn wir für jede der Personen eine Liste von Gewichten
# bekommen könnten.
# Dabei hilft uns das Dictionary.

# %%
# Ein Dictionary wird mit `{}`-Klammern geschrieben.
# Es ordnet einem Schlüssel (Key, links vom `:`) einen Wert (Value, rechts vom
# `:`) zu
# Zu jedem Schlüssel gibt es nur einen Wert.
# Eine schöne Analogie ist ein Telefonbuch;
# für jeden Namen ist eine Nummer hinterlegt:

adressbuch = {
    "Feuerwehr": "110",
    "Polizei": "112",
    "Herrmann": "07543 73135",
    "Caro": "07314 93849193",
}

# Um die Nummer von jemandem zu bekommen, kann man per `[]`
# darauf zugreifen:
adressbuch["Polizei"]

# %%
# Ebenso kann man einen Wert ändern
adressbuch["Caro"] = "07314 4815"
# oder hinzufügen:
adressbuch["Paul"] = "07321 37294"

# %%
# Um zu prüfen, ob ein Eintrag für einen bestimmten Schlüssel vorliegt, prüft
# man mit `in`:
"Paul" in adressbuch

# %%
# Die Werte in einem Dictionary können auch selbst komplexere Objekte sein, wie
# bspw. eine Liste.
# Füge für "Wolfgang" eine Liste mit den Nummern "0176 84927413" und "07421
# 39495" hinzu.


# %%
# Genug mit Vorgeplänkel, jetzt zur eigentlichen Aufgabe.
# Vervollständige die folgende Funktion, sodass sie eine Datei mit dem gleichen
# Format wie `beispieldaten_gewichte.txt` einließt und als Ergebnis ein Dict
# ausgibt, das die Namen der gewogenen als Schlüssel und als Werte eine Liste
# von Gewichten als Zahl (`int`) hat.
#
# Bspw. erzeugt
#    extrahiere_gewichte("beispieldaten_gewichte.txt")
# den Output
#    {'Herrmann': [72, 73, 71, 74],
#     'Caro': [62, 60, 59, 60, 61, 60]}
#
# Hinweis: Verwende am besten Code von gestern wieder!


from typing import Dict, List
import re

def extrahiere_gewichte(dateiname: str) -> Dict[str, List[int]]:
    pass