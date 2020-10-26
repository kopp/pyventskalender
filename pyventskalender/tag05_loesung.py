from .tag05 import ich_tippe_auf


def finde_zufallszahl():
    geraten = 10
    while True:
        tip = ich_tippe_auf(geraten)
        # Um zu sehen, wie der Algorithmus arbeitet, kann man folgendes machen:
        # print("{} -> {}".format(geraten, tip))
        if tip.startswith("richtig"):
            return geraten
        else:
            if tip.endswith("hoch"):
                geraten = geraten - 1
            else:
                geraten = geraten + 1

