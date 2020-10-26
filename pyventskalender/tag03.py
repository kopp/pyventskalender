# Python unterscheidet zwischen verschiedenen Datentypen.
# Verschidene Datentypen haben verschiedene Eigenschaften und Fähigkeiten.
# Beispielsweise gibt es in Python fest eingebaute einfache Typen
# - ganze Zahlen, `int`, mit denen man Dinge Zählen kann -- bspw. 1, 47
# - Kommazahlen, `float`, mit denen man rechnen kann -- bspw. 3.1415
# - Text, `str`, den man formatieren, ausgeben oder zusammensetzen kann --
#   bspw. "Katze".
#   Auch im Deutschen verwendet man für Text in der Programmierung den namen
#   "String".
# - Wahrheitswerte, `bool`, die nur sagen können, ob etwas wahr (`True`) oder
#   falsch (`False`) ist

# %%
# Um sich jederzeit klar zu machen, was für einen Typ eine Variable hat, kann
# man dies an der Variablen notieren:

tierart: str = "Katze"

# %%
# Man kann es aber auch zur Laufzeit herausfinden, indem man die Funktion
# `type()` auf eine Variable anwendet:

type(tierart)

# %%
# Die Notation von Typen kann man auch an Funktionen machen.
# Hier kann man den Typ des Parameters notieren.
# Ebenso, kann man den Typ des Returnwerts per `->` hinter die
# Funktion schreiben:

def sprich_ueber_haustiere(name_deiner_mutter: str, anzahl_katzen: int) -> str:
    text: str = "Meine Mutter {} hat {} Katzen.".format(name_deiner_mutter, anzahl_katzen)
    return text

# Hier sehen wir auch schon etwas, das man mit Strings machen kann:
# Man kann sie formatieren.
# Die Methode `.format()` ersetzt alle `{}` in dem String durch die Werte, die
# man ihr als Parameter mitgibt.
#
# Allgemein ist eine Methode etwas, das man mit der `.`-Notation auf ein Objekt
# anwenden kann -- also `objekt.methodenname(parameter)`.

# %%
# Jetzt kommt die (erste) Herausforderung:
# Schreibe eine Funktion, die als Argument einen String (Tierart im Plural)
# entgegennimmt und als Ausgabe den Text "Ich mag <TIERNAME>" ausgibt.
# Der Tiername soll dabei in Großbuchstaben ausgegeben werden.
# Dabei kann die Methode `upper` helfen (`"foo".upper() -> "FOO"`).
# Beispielsweise soll
#    ich_mag("Katzen")
# den Text "Ich mag KATZEN." ausgeben.

def ich_mag():
    pass

# %%
# Wenn das geschafft ist, wollen wir noch Zahlen dazu nehmen.
# In der folgenden Funktion soll man zwei verschiedene Tierarten und die
# jeweilige Anzahl angeben können, bspw.
#     def ich_will(5, "Katzen", 3, "Hunde")
# und die Ausgabe soll daraus wieder einen Satz machen:
#     "Ich mag 5 KATZEN und 3 HUNDE!.".format(

def ich_will():
    pass

# %%
# Und als letzte Aufgabe heute wollen wir noch etwas rechnen.
# Die Folgende Funktion soll berechnen, wie viel Futter eine bestimmte Anzahl
# von Hamstern und Fischen am Tag isst.
# Dazu sind die beiden Werte gegeben, was ein einzelnes Tier pro Tag frisst:

MASSE_FUTTER_HAMSTER_PRO_TAG_IN_G = 23.5
MASSE_FUTTER_FISCH_PRO_TAG_IN_G = 12.25

# (In Python schreibt man per Konvention Daten, die sich nicht ändern, mit
# Großbuchstaben.)
# Die Funktion soll die Anzahl von Hamnstern und Fischen entgegennehmen und die
# Menge an Futter (insgesamt) ausgeben.

def futterration_berechnen(anzahl_hamster, anzahl_fische):
    pass

# %%