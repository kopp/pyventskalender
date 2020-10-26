# Ein wichtiger Baustein in der Programmierung ist die Verzweigung, also die
# Wenn-Dann-Beziehung.
# Dabei wird geprüft, ob (`if`) eine bestimmte Bedingung wahr ist.
# Ist dem so, so wird ein bestimmter Code-Block ausgeführt.
# Ist dem nicht so (`else`), wird optional ein anderer Code-Block ausgeführt.
# Optional bedeutet dabei, dass man auf diesen Teil auch verzichten kann.
# Zudem kann man in dem Dann-Teil noch weitere Abfragen einbauen, also eine
# Wenn-Dann-und-zusätzlich-sonst-Abfrage.
# Diese wird mit `elif` geschrieben.
# Davon kann man beliebig viele haben.

#%%
# Ein Beispiel:

def tiergeraeusch(tier: str) -> str:
    if tier == "Katze":
        return "Miau"
    elif tier == "Elefant":
        return "Törööö"
    else:
        return "Keine Ahnung wie ein {} macht".format(tier)

tiergeraeusch("Affe")

#%%
# Die einfachsten Abfragen, die man machen kann, sind Vergleiche:
# - Gleichheit: `==`
# - Kleiner: `<`
# - Kleiner oder gleich: `<=`
# - Größer: `>`
# - Größer oder gleich: `>=`
#
# Damit kommen wir zur ersten Herausforderung:
# Vervollständige die folgende Funktion so, dass sie angibt, dass man entweder
# eine Katze möchte oder mehrer Katzen.
# Ausgabe soll bspw. sein:
#    "Ich hätte gerne 4 Katzen"  # Hat noch ein n
#    "Ich hätte gerne 1 Katze"   # Hat kein n
def ich_haette_gerne_so_viele_katzen(anzahl: int) -> str:
    pass

#%%
# Man kann aber auch Methoden und Funktionen abfragen.
# Beispielsweise haben Strings die Methode `.startswith()`, die prüft, ob ein
# String mit einem anderen Beginnt.
# Beispielsweise kann man herausfinden, ob ein Wort mit "Zucker" beginnt, indem
# man

def ist_sicher_lecker_aber_ungesund(essen: str) -> bool:
    if essen.startswith("Zucker"):
        return "ja, {} ist vermutlich ungesund".format(essen)
    else:
        return "man weiß es bei {} nicht...".format(essen)

ist_sicher_lecker_aber_ungesund("Zuckerwatte")

# %%
# Damit können wir schon ein kleines Spiel bauen.
# Hier wird eine Zufallszahl zwischen 1 und 20 gewählt:
import random
zufallszahl = random.randint(1, 20)

# Die folgende Funktion soll ausgeben
# - "richtig, gefunden!" wenn man die korrekte Zahl angibt
# - "falsch, zu hoch", wenn die gesuchte Zahl niedriger ist oder
# - "falsch, zu niedrig", wenn die gesuchte Zahl höher ist
# Damit kann man dann immer wieder mit bspw. `ich_tippe_auf(5)` einen Tip
# abgeben, und die Funktion sagt, wie man weiter raten muss.
# Ein solches Spiel könnte dann so ablaufen:
#    ich_tippe_auf(5) -> 'falsch, zu niedrig'
#    ich_tippe_auf(10) -> 'falsch, zu hoch'
#    ich_tippe_auf(7) -> 'richtig, gefunden!'

def ich_tippe_auf(zahl: int):
    pass
