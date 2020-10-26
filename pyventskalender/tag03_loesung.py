
tierart: str = "Katze"

type(tierart)

def sprich_ueber_haustiere(name_deiner_mutter: str, anzahl_katzen: int) -> str:
    text: str = "Meine Mutter {} hat {} Katzen.".format(name_deiner_mutter, anzahl_katzen)
    return text

def ich_mag(tiere: str) -> str:
    return "Ich mag {}.".format(tiere.upper())

def ich_will(anzahl1: int, tiere1: str, anzahl2: int, tiere2: str) -> str:
    return "Ich mag {} {} und {} {}!.".format(
        anzahl1, tiere1.upper(), anzahl2, tiere2.upper())

MASSE_FUTTER_HAMSTER_PRO_TAG_IN_G = 23.5
MASSE_FUTTER_FISCH_PRO_TAG_IN_G = 12.25

def futterration_berechnen(anzahl_hamster, anzahl_fische):
    futter_hamster = MASSE_FUTTER_HAMSTER_PRO_TAG_IN_G * anzahl_hamster
    futter_fische = MASSE_FUTTER_FISCH_PRO_TAG_IN_G * anzahl_fische
    futter_gesamt = futter_hamster + futter_fische
    return futter_gesamt