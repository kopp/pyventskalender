# Heute wollen wir die Worte richtig zufällig auswählen.


# %%
# Holen wir uns mal die Wort-Listen von gestern
try:
    from pyventskalender.tag18 import MOEGLICHE_OBJEKTE, MOEGLICHE_SUBJEKTE, MOEGLICHE_VERBEN, MOEGLICHE_ADVERBIALE
except ImportError:
    from tag18 import MOEGLICHE_OBJEKTE, MOEGLICHE_SUBJEKTE, MOEGLICHE_VERBEN, MOEGLICHE_ADVERBIALE


# %%
# Die Funktion `choice` wählt zufällig ein Element aus einer Menge aus:
from random import choice
beispiel_verb = choice(MOEGLICHE_VERBEN)

# %%
# So weit sind wir gestern mit unseren beiden Klassen gekommen

class Satzglied:
    def __init__(self, moeglichkeiten):
        self.moeglichkeiten = moeglichkeiten
        self.text = self.moeglichkeiten[0]

class Satz:
    def __init__(self):
        self.adverbiale = Satzglied(MOEGLICHE_ADVERBIALE)
        self.verb = Satzglied(MOEGLICHE_VERBEN)
        self.subjekt = Satzglied(MOEGLICHE_SUBJEKTE)
        self.objekt = Satzglied(MOEGLICHE_OBJEKTE)


# %% Methode hinzufügen -- Test 10
# Erstelle jetzt eine Methode `zufaelliges_neues` in `Satzglied`, die ein neues
# Element aus der Liste `self.moeglichkeiten` wählt und in `text` schreibt.
# Du kannst das testen, indem du dir ein `Satzglied` erzeugst und die Funktion
# immer wieder aufrufst -- es sollten verschiedene Ergebnisse raus kommen, wenn
# man die Methode mehrmals aufruft.


# %% Methode hinzufügen -- Test 20
# Um jetzt einen Zufallssatz zu bekommen, spendiere dem `Satz` bitte eine
# Methode `zufaelligen_neuen`, der jedes Wort zufällig neu auswählt.


# %% __str__ Methode -- Test 30
# Jetzt wollen wir den Satz endlich ausgeben.
# Um Objekte als `str` auszugeben, füge eine Funktion `__str__` in `Satz`
# hinzu, die einen `str` zurück gibt -- unseren Satz, bestehend aus den
# einzelnen Worten, durch Leerzeichen getrennt und mit einem Punkt hinten.


# %%
# Geschafft -- jetzt gönnen wir uns ein paar nette Sätze:

def saetze():
    satz = Satz()
    for i in range(5):
        satz.zufaelligen_neuen()
        print(satz)
        print()
# %%