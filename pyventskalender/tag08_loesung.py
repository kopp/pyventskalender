from typing import List

BEKANNTE_SAEUGETIERE = [
    "Hund",
    "Katze",
    "Affe",
    "Mensch",
    "Maulwurf",
    "Pferd",
]


def saeugetiere_aus(tiere: List[str]) -> List[str]:
    saeugetiere = []
    for tier in tiere:
        if tier in BEKANNTE_SAEUGETIERE:
            saeugetiere.append(tier)
    return saeugetiere


def mensch_mag_tier(menschen: List[str], tiere: List[str]) -> List[str]:
    mag = []
    for mensch in menschen:
        for tier in tiere:
            mag.append("{} mag {}".format(mensch, tier))
    return mag
