# Heute geht es mit dem Galgenmännchen weiter.
#
# Setzt Datei pyventskalender/galgenmannbilder.py voraus.

# %%
# Importieren wir erst mal, was wir gestern geschafft haben.
# Dabei müssen wir wieder den Trick anwenden, doppelt zu importieren -- einmal
# wie man es in Python eben machen sollte ...

try:
    from pyventskalender.tag14_loesung import VERLOREN_BEI_SO_VIELEN_FEHLERN
# ... und falls man direkt in Visual Studio Code arbeitet nochmal ohne Pfad:
except ImportError:
    from tag14_loesung import VERLOREN_BEI_SO_VIELEN_FEHLERN

# %% Prüfe Eingabe -- Tests 10 20 30
# Heute geht es damit weiter, dass wenn wir einen Nutzer nach einem geratenen
# Buchstaben fragen, wir nicht unbedingt auch bekommen, was wir wollen.
# Statt nur einen Buchstaben zu erraten, könnte er auch `"hallodu"` eingeben.
# Definiere deshalb eine Funktion `ist_buchstabe` die eine Eingabe als `str`
# entgegennimmt und ausgibt, ob es sich um genau ein Zeichen handelt (und nicht
# mehr oder weniger).
# Bitte annotiere dabei die Typen der Eingabe und des Rückgabewerts.

# def ...


# %% Prüfe ob Spieler aufgibt -- Tests 40 50
# Außerdem wollen wir dem Spieler die Möglichkeit geben, aufzugeben.
# Schreibe deshalb eine Funktion `ist_aufgeben`, die wieder eine Nutzereingabe
# bekommt und sagt, ob es sich dabei um den Text `"ich gebe auf"` handelt --
# dabei soll die Groß/Kleinschreibung keine Rolle spielen (also "Ich geben auf"
# und "ICH GEBE auf" usw. soll gleich als Aufgabe bewertet werden).

# def ...


# %%
# Jetzt noch eine Letzte Vorbereitung.
# Wir wollen die Datenstruktur Menge, `set`, kennen lernen.
# In einer Menge kann jedes Element vorkommen oder nicht -- aber nicht
# mehrmals.
# Außerdem hat es keine "Position" in der Menge -- also man kann nur sagen, ob
# das Element vorhanden ist, oder nicht.
# Man erzeugt eine Menge per `set()`, beispielsweise
set([1, 2, 3])
# Hier wird die Menge aus einer Liste erzeugt.
# Die Informationen über Reihenfolge oder Anzahl gehen dabei verloren:
set([1, 2, 3]) == set([3, 1, 2]) == set([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3])

# %%
# Die sinnvollen Operationen, die man mit einer Menge durchführen kann, sind:
# Ist ein Element in der Menge?
"foo" in set(["foo", "bar"])

# %%
# Elemente hinzufügen
was_ich_kann = set(["Laufen", "Radfahren"])
was_ich_kann.add("Python")

# %%
# Elemente entfernen
was_ich_kann.remove("Laufen")


# %% Bewerte Eingabe -- Tests 60 70
# Das können wir gleich verwenden.
# Vervollständige die folgende Funktion, die einen neuen geratenen Buchstaben
# entgegennimmt.
# Sie soll bewerten, ob er passend geraten ist (wenn er in
# `noch_gesuchte_buchstaben` ist) oder nicht.
# Wenn der Buchstabe korrekt gefunden ist, dann soll er aus den
# `noch_gesuchte_buchstaben` entfernt werden, wenn er falsch geraten war, soll
# er an die Liste `falsch_geratene_buchstaben` angehängt werden.
# - Sollte es gelungen sein, alle Buchstaben zu finden, dann soll die Funktion
#   `"gewonnen"` zurück geben.
# - Sollten zu viele Buchstaben schon falsch geraten worden sein
#   (`VERLOREN_BEI_SO_VIELEN_FEHLERN`), soll sie `"verloren"` zurück geben.
# - Sonst soll sie `"richtig-geraten"` bzw. `"falsch-geraten"` zurück geben.

from typing import Set, List, Optional

def bewerte_geratenen_buchstaben(
    buchstabe: str,
    noch_gesuchte_buchstaben: Set[str],
    falsch_geratene_buchstaben: List[str]
    ) -> Optional[bool]:
    pass


# %%
# So, das war es schon fast.  Morgen schaffen wir es.