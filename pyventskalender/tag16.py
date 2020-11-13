# %%

try:
    from pyventskalender.tag14_loesung import zu_ratendes_wort, galgenmannbild
    from pyventskalender.tag15_loesung import ist_aufgeben, ist_buchstabe, bewerte_geratenen_buchstaben
# ... und falls man direkt in Visual Studio Code arbeitet nochmal ohne Pfad:
except ImportError:
    from tag14_loesung import zu_ratendes_wort, galgenmannbild
    from tag15_loesung import ist_aufgeben, ist_buchstabe, bewerte_geratenen_buchstaben


def galgenmannspiel(gesuchtes_wort: str):
    gesuchtes_wort = gesuchtes_wort.strip()
    noch_gesuchte_buchstaben = set(gesuchtes_wort.lower())
    falsch_geratene_buchstaben = []
    while True:
        print("Gesucht: ", zu_ratendes_wort(gesuchtes_wort, noch_gesuchte_buchstaben))
        eingabe = input("Rate einen Buchstaben")
        if ist_aufgeben(eingabe):
            break
        if not ist_buchstabe(eingabe):
            continue
        buchstabe = eingabe.strip().lower()
        bewertung = bewerte_geratenen_buchstaben(buchstabe, noch_gesuchte_buchstaben, falsch_geratene_buchstaben)
        if bewertung == "richtig-geraten":
            print("Gut geraten!")
        elif bewertung == "falsch-geraten":
            print("{} ist leider falsch; bisher falsch geraten: {}".format(
                buchstabe,
                falsch_geratene_buchstaben))
            print(galgenmannbild(len(falsch_geratene_buchstaben)))
        elif bewertung == "gewonnen":
            print("Erraten!  Das Wort war {}".format(gesuchtes_wort))
            return True
        elif bewertung == "verloren":
            print("Leider nicht geklappt -- das Wort war {}".format(gesuchtes_wort))
            print(galgenmannbild(len(falsch_geratene_buchstaben)))
            return False