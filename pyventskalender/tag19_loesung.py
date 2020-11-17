try:
    from pyventskalender.tag18 import MOEGLICHE_OBJEKTE, MOEGLICHE_SUBJEKTE, MOEGLICHE_VERBEN, MOEGLICHE_ADVERBIALE
except ImportError:
    from tag18 import MOEGLICHE_OBJEKTE, MOEGLICHE_SUBJEKTE, MOEGLICHE_VERBEN, MOEGLICHE_ADVERBIALE


class Satzglied:
    def __init__(self, moeglichkeiten):
        self.moeglichkeiten = moeglichkeiten
        self.text = self.moeglichkeiten[0]

    def zufaelliges_neues(self):
        self.text = choice(self.moeglichkeiten)

class Satz:
    def __init__(self):
        self.adverbiale = Satzglied(MOEGLICHE_ADVERBIALE)
        self.verb = Satzglied(MOEGLICHE_VERBEN)
        self.subjekt = Satzglied(MOEGLICHE_SUBJEKTE)
        self.objekt = Satzglied(MOEGLICHE_OBJEKTE)

    def zufaelligen_neuen(self):
        self.adverbiale.zufaelliges_neues()
        self.verb.zufaelliges_neues()
        self.subjekt.zufaelliges_neues()
        self.objekt.zufaelliges_neues()

    def __str__(self):
        return "{} {} {} {}.".format(
            self.adverbiale.text,
            self.verb.text,
            self.subjekt.text,
            self.objekt.text,
        )