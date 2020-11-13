# Setzt Datei pyventskalender/galgenmannbilder.py voraus.

try:
    from pyventskalender.galgenmannbilder import HANGMANPICS
except ImportError:
    from galgenmannbilder import HANGMANPICS


def galgenmannbild(anzahl_fehler: int) -> str:
    return HANGMANPICS[anzahl_fehler]


VERLOREN_BEI_SO_VIELEN_FEHLERN = len(HANGMANPICS) - 1


def zu_ratendes_wort(gesuchtes_wort, fehlende_buchstaben):
    anzuzeigendes_wort = gesuchtes_wort
    for fehlender_buchstabe in fehlende_buchstaben:
        anzuzeigendes_wort = anzuzeigendes_wort.replace(fehlender_buchstabe.upper(), "_")
        anzuzeigendes_wort = anzuzeigendes_wort.replace(fehlender_buchstabe.lower(), "_")
    return anzuzeigendes_wort
