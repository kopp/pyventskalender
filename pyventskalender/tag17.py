# Heute soll es darum gehen, eigene Typen zu erstellen.

# %%
# In Python wird ein Typ, eine Klasse, mit `class <Name>` angelegt.
# Per Konvention schreibt man Typen groß.
# Der Typ wird dadurch nutzbar, dass man ihm eigene Daten und Methoden gibt --
# das sind die Dinge, die man mit ihm machen kann.
# Eine Methode ist eine Funktion, die auf ein Objekt des Typs angewendet werden
# kann.
# Damit sie auf die Daten des Objekts zugreifen kann, bekommt jede Methode als
# ersten Parameter `self`, was das Objekt selbst beinhaltet.
class Katze:
    def __init__(self, name):
        self.name = name

    def macht_ton(self):
        return "Miauuuuu"


# %%
# Die Methode `__init__` ist speziell: Sie wird aufgerufen, wenn das Objekt
# erstellt wird.
# Sie bekommt als Parameter den `name` der Katze und speichert ihn direkt als
# `self.name`.
mauzi = Katze("Mauzi")

# %%
# Damit hat unsere Katze die erste Eigenschaft, die wir abrufen können
mauzi.name

# %%
# Die zweite Methode gibt der Katze etwas, das sie machen kann: einen Ton.
mauzi.macht_ton()


# %%
# Jetzt erstellen wir mal ein paar Katzen:
katzen = [
    Katze("Felix"),
    Katze("Bommel"),
    Katze("Garfield"),
]


# %% Methoden aufrufen -- Test 20
# Vervollständige jetzt die folgende Funktion so, dass sie eine Liste von
# Katzen entgegen nimmt und jede davon einen Ton machen lässt; das soll in
# einen `str` zusammengefasst und ausgegeben werden.
# Mache hinter jedem Ton bitte ein Leerzeichen, damit man die einzelnen Rufe
# auseinander halten kann.

def katzenkonzert_von(katzen):
    return ""


# %% Methode und Argument kombinieren -- Test 30
# Das ist noch recht unübersichtlich -- modifiziere bitte `macht_ton` so, dass
# die Ausgabe den Namen enthält, also "Felix macht Miauuuuu" für Felix usw.


# %% Methode hinzufügen -- Test 40
# Und jetzt erweitere die Klasse `Katze` um eine Methode `frisst`, die als
# Parameter ein Essen entgegennimmt.
# Das Essen soll im Magen der Katze (eine Liste `self.magen`) gespeichert
# werden und die Ausgabe soll sein "<Name> mag <Essen>", also bspw. "Felix mag
# Maus".


# %% Member anlegen -- Test 50
# Jede Methode kann neue Daten an das Katze-Objekt hängen.
# Es ist also völlig legitim, den `magen` erst in `frisst` anzulegen.
# Schöner ist es aber, wenn die Katze schon mit Magen "erschaffen" wird.
# Dazu kann man in der `__init__`-Funktion den Magen als Leere Liste anlegen.