# Eine Funktion ist eine kurze Liste von Befehlen.
# Die Funktion hat einen Namen, damit kann man sie aufrufen.
# Ist der Name gut gewählt, kann man auch verstehen, was die Funktion
# eigentlich macht.
# Damit kann man seine Programme übersichtlicher gestalten, indem man
# - Befehle/Algorithmen, die sich an mehreren Stellen im Programm wiederholen,
#   nur einmal programmieren muss, und dann immer wieder verwenen kann (indem man
#   die Funktion aufruft)
# - Den Funktionen gute Namen gibt, sodass man alleine durchs Lesen versteht,
#   was der Code macht.
#
# Zusätzlich kann man den Funktionen Parameter mitgeben.
# Das sind verschiedene Werte, die die Funktion als Eingabe nimmt.
# Jeder der Parameter hat einen Namen.
# Die Funktion kann etwas mit den Parametern machen, und ein Ergebnis
# zurückgeben.
# Dazu wird das Wort `return` verwendet.
#
# %%
# Beispielsweise könnte eine Funktion so aussehen:

def addiere_zahlen(a, b):
    summe = a + b
    return summe

# Das `def` signalisiert, dass hier eine neue Funktion definiert wird.
# In Klammern stehen die Parameter, durch Kommas getrennt.
#
# Diese Funktion kann jetzt aufgerufen werden.
# Dazu schreibt man den Namen und in Klammern Werte für die Parameter.
# Um den Rückgabewert zu speichern, weist man diesen einer neuen Variablen zu:

drei = addiere_zahlen(1, 2)
addiere_zahlen(drei, 1)  # ergibt 4, aber das speichern wir nirgends

# Um diese Funktion jetzt auszuprobieren, kann man auf "Run Cell" klicken.
# Die Funktion ist dann in dem interaktiven Fenster definiert.
# Man kann sie dort verwenden, indem man in der Eingabezeile bspw.
#    addiere_zahlen(23, 7)
# eintippt und dann Shift+Enter drückt.
#
# Wichtiger Tip: Per Tab kann man sich seine Eingaben vervollständigen lassen.
# Es reicht also bspw. `addie` zu tippen und dann Tab zu drücken.

# %%
# Funktionen können in anderen Funktionen aufgerufen werden:

def bilde_durchschnitt(a, b, c, d, e):
    summe = addiere_zahlen(a, b)
    summe = addiere_zahlen(c, summe)
    summe = addiere_zahlen(d, summe)
    summe = addiere_zahlen(e, summe)
    return summe/5

# Das ist natürlich nicht besonders sinnvoll.
# %%
# Wenden wir uns etwas sinnvollerem zu: Wenn Tiere rechnen.
# Die Folgende Funktion erzeugt eine bestimmte Anzahl von Mööös.
# Der Text in den """Anführungszeichen""" ist ein Docstring -- damit kann man
# beschreiben, was die Funktion macht.

def elchgeraeusch(wiederholungen):
    """Gibt einen String mit einer bestimmten Anzahl an Mööös aus."""
    elchausspuch = ""
    for i in range(wiederholungen):  # das wird einfach wiederholungen-mal ausgeführt
        elchausspuch += "Mööö "  # a += b  bedeutet  a = a + b
    return elchausspuch

# %%
# Jetzt vervollständige bitte eine Funktion, die das gleiche für mit Kazten
# macht.
# Katzen machen "Miau".
# Hinweis: `pass` bedeutet: das muss noch durch "echten" Code ersetzt werden.

def katzengeraeusch():
    pass

# %%
# Jetzt lassen wir die Tiere rechnen.
# Hinweis: Zwei Strings kann man per "+" zusammensetzen, bspw.
zusammengesetzter_text = "Hallo " + "Welt" + "!"

def addiere(elchrufe, katzenrufe):
    """
    Gib einen String mit zuerst `elchrufe` mal Mööö und dann `katzenrufe` mal
    Miau aus.
    """
    pass


# %%
# Wir können auch zählen, wie oft hier gerufen wird:

def zaehle_tierlaute(tierrufe):
    # Zerlege die Strings bei Leerzeichen
    laute = tierrufe.strip().split(" ")
    # Lösche leere Strings (sind ja keine Laute)
    if "" in laute:
        laute.remove("")
    # Zähle die Anzahl von Lauten
    anzahl_laute = len(laute)
    return anzahl_laute


# %%
# Damit können wir jetzt rechnen:

def subtrahiere_elchrufe_von_katzenrufen(elchrufe, katzenrufe):
    """
    Subtrahiert von der Anzahl von Elchrufen die Anzahl von Katzenrufen und
    gibt diese als Elchrufe aus.

    Also beispielseweise könnte der Input
    "Mööö Mööö Mööö " und "Miau Miau " sein, dann würde als Ergebnis
    "Mööö " erwartet.
    """
    pass

# %%