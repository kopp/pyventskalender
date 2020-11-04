# Wir wollen jetzt aus der Gewichtsdatei die Namen und Gewichte extrahieren.

# %%
# Um so eine Zeile zu verarbeiten, kann man Regular Expressions verwenden.
# Diese kann man sich wie eine Schablone vorstellen, die man über Text legt und
# dann bestimmte Stellen des Texts hervorgehoben bekommt.
# Die folgende Regular Expression passt zu Texten wie
#    Tobias mag Hunde
#    (....) mag (...)
#    Fernstrassen zu bauen mag komplex sein
#    (...................) mag (..........)

import re
mag_re = re.compile(r"(.*) mag (.*)")

# Das `.*` bedeutet _keines oder mehrere Zeichen_.
# `...` würde bedeuten: 3 Zeichen (der `.` steht für jedes Zeichen).
# Ein `.+` würde bedeuten: _eines oder mehrere Zeichen_.
# Um einen `.` im Text zu suchen, verwendet man `\.`.
# (Bspw. passt r"." auf "x" und ".", aber r"\." passt nur auf ".", nicht auf
# "x".)
# Die Klammern sorgen dafür, dass man die Teile des Texts, auf die die
# Schablone passt, zurückbekommen kann; diese Teile werden als Gruppe
# bezeichnet.

def etwas_moegen(text: str):
    gefunden = mag_re.match(text)
    if gefunden:
        subjekt = gefunden.group(1)
        objekt = gefunden.group(2)
        print("{} scheint zu mögen: {}".format(subjekt, objekt))
    else:
        print("In '{}' geht es nicht ums Mögen".format(text))


# Hinweis: `import re` sorgt dafür, dass man die Regular Expresions verwenden
# kann.
# zahlen einlesen
# durchschnitt bilden

# %%
# Schreibe jetzt eine Funktion, die die Gewichte-Datei Zeile für Zeile ließt
# und jeweils Name und Gewicht extrahiert.
# Die Ausgabe erfolgt als Liste, die für jede übersetzte Zeile wieder eine
# Liste mit Name und Gewicht enthält, also bspw. erzeugt
#    extrahiere_gewichte("beispieldaten_gewichte.txt")
# den Output
#    [['Herrmann', '72'],
#     ['Caro', '62'],
#     ['Herrmann', '73'],
#     ['Caro', '60'],
#     ... ]
#
# Hinweis: Um eine Regular expression zu testen, ist es hilfreich, das in der
# interaktiven Konsole zu machen.
# Dazu schreibt man in der Konsole bspw.
#     re.compile(r"foo (...) asdf").match("foo bar asdf")
# Ist das Ergebnis `None`, dann passt die Regular Expression noch nicht zum
# eingegebenen Text.
# Hat man es geschafft, dass die Regular Expression zum Text passt, kann man
# als nächstes die Gruppen untersuchen, bspw. per
#     re.compile(r"foo (...) asdf").match("foo bar asdf").groups()
# In der interaktiven Konsole kann man dann immer wieder die vorherige Zeile
# per Pfeiltaste nach oben aufrufen, leicht modifizieren und wieder versuchen.
#
# Hinweis: Die Tests zu dieser Funktion verwenden nicht nur die Beispieldaten,
# sondern auch anderen Daten!

from typing import List
import re

def extrahiere_gewichte(dateiname: str) -> List[List[str]]:
    pass


# %%
# Jetzt noch eine Kleinigkeit: Wenn man Regular Expressions verwendet, dann
# versteht der Code nicht, ob man eine Zahl oder Text aus einem Text
# extrahiert.
# Um aus dem Text "1" die Zahl 1.0 zu machen, verwendet man `float("1")`.
# Vervollständige die folgende Funktion, die die Ausgabe von
# `extrahiere_gewichte` nimmt und die Gewichte jeweils in Zahlen `float`s)
# umwandelt.

from typing import List, Union

def gewichte_als_zahlen(gewichte: List[List[str]]) -> List[List[Union[str, float]]]:
    pass

# %%
# Die beiden Funktionen müsste man jetzt zusammenschalten können:

def zeige_gewichte():
    print(gewichte_als_zahlen(extrahiere_gewichte("beispieldaten_gewichte.txt")))
# %%
