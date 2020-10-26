from typing import List

unverstanden = []


def frage_nach_lieblingstieren() -> List[str]:
    tiere = []
    while len(tiere) < 3:
        neues_tier = input("Nenne ein Lieblingstier")
        if neues_tier in tiere:
            print("{} hattest du schon gesagt.".format(neues_tier))
        else:
            tiere.append(neues_tier)
    return tiere


def platz_auf_siegertreppchen(siegertiere: List[str], einzelnes_tier: str):
    if einzelnes_tier not in siegertiere:
        return None
    else:
        if einzelnes_tier == siegertiere[0]:
            return 1
        if einzelnes_tier == siegertiere[1]:
            return 2
        if einzelnes_tier == siegertiere[2]:
            return 3