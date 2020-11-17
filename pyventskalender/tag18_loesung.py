MOEGLICHE_ADVERBIALE = [
    "Beim Programmieren",
    "Am PC",
    "Im ICE",
    "An der Kasse",
    "Beim Schaukeln",
    "Bei Vollmond",
    "Auf dem Weihnachtsmarkt",
]

MOEGLICHE_VERBEN = [
    "liebt",
    "kontrolliert",
    "sucht",
    "springt",
    "schenkt mir",
    "vergisst",
    "lobt",
]

MOEGLICHE_SUBJEKTE = [
    "meine Frau",
    "der Schaffner",
    "jeder",
    "der 7. Zwerg",
    "die Verkäuferin",
    "das Nachbarskind",
]

MOEGLICHE_OBJEKTE = [
    "Python",
    "frische Kräuter",
    "die roten Schuhe",
    "einen Kaugummi",
    "den neuen Hut",
    "einen Bademantel",
    "den Busfahrer",
]


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