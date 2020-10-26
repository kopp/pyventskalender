def addiere_zahlen(a, b):
    summe = a + b
    return summe

def bilde_durchschnitt(a, b, c, d, e):
    summe = addiere_zahlen(a, b)
    summe = addiere_zahlen(c, summe)
    summe = addiere_zahlen(d, summe)
    summe = addiere_zahlen(e, summe)
    return summe/5


def elchgeraeusch(wiederholungen):
    """Gibt einen String mit einer bestimmten Anzahl an Mööös aus."""
    elchausspuch = ""
    for i in range(wiederholungen):
        elchausspuch += "Mööö "
    return elchausspuch

def katzengeraeusch(wiederholungen):
    katzenausspuch = ""
    for i in range(wiederholungen):
        katzenausspuch += "Miau "
    return katzenausspuch
    # Könnte man auch einfach schreiben als
    return wiederholungen * "Miau "


def addiere(elchrufe, katzenrufe):
    """
    Gib einen String mit zuerst `elchrufe` mal Mööö und dann `katzenrufe` mal
    Miau aus.
    """
    elchspruch = elchgeraeusch(elchrufe)
    katzenspruch = katzengeraeusch(katzenrufe)
    summe = elchspruch + katzenspruch
    return summe
    # Könnte man auch einfach schreiben als
    return elchgeraeusch(elchrufe) + katzengeraeusch(katzenrufe)


def zaehle_tierlaute(tierrufe):
    # Zerlege die Strings bei Leerzeichen
    laute = tierrufe.strip().split(" ")
    # Lösche leere Strings (sind ja keine Laute)
    if "" in laute:
        laute.remove("")
    # Zähle die Anzahl von Lauten
    anzahl_laute = len(laute)
    return anzahl_laute


def subtrahiere_elchrufe_von_katzenrufen(elchrufe, katzenrufe):
    """
    Subtrahiert von der Anzahl von Elchrufen die Anzahl von Katzenrufen und
    gibt diese als Elchrufe aus.

    Also beispielseweise könnte der Input
    "Mööö Mööö Mööö " und "Miau Miau " sein, dann würde als Ergebnis
    "Mööö " erwartet.
    """
    anzahl_elchrufe = zaehle_tierlaute(elchrufe)
    anzahl_katzenrufe = zaehle_tierlaute(katzenrufe)
    differenz = anzahl_elchrufe - anzahl_katzenrufe
    differenz_als_elchruf = elchgeraeusch(differenz)
    return differenz_als_elchruf
