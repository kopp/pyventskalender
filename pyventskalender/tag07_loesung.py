
def kuehe_machen_muehe(anzahl: int) -> str:
    if anzahl == 0:
        return "0 Kühe machen keine Mühe"
    elif anzahl == 1:
        return "1 Kuh macht Muh"
    else:
        return "{} Kühe machen {} mal Mühe".format(anzahl, anzahl)

def kuh_sinnsprueche(anzahl_min: int, anzahl_max: int) -> None:
    """
    Gib den Sinnspruch der Funktion `kuehe_machen_muehe` für alle
    Kuh-Anzahlen zwischen `anzahl_min` und `anzahl_max` aus.
    (Also bei anzahl_min=5 und anzahl_max=7 wird der Text für 5, 6, und 7
    ausgegeben.)
    """
    for anzahl in range(anzahl_min, anzahl_max + 1):
        print(kuehe_machen_muehe(anzahl))
