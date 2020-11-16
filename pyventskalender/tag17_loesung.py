
class Katze:
    def __init__(self, name):
        self.name = name
        self.magen = []

    def macht_ton(self):
        return "{} macht Miauuuuu".format(self.name)

    def frisst(self, essen: str) -> str:
        self.magen.append(essen)
        return "{} mag {}".format(self.name, essen)


katzen = [
    Katze("Felix"),
    Katze("Bommel"),
    Katze("Garfield"),
]


def katzenkonzert_von(katzen):
    gesang = ""
    for katze in katzen:
        gesang += katze.macht_ton()
        gesang += " "
    return gesang