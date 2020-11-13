from typing import Set, List, Optional

try:
    from pyventskalender.tag14_loesung import VERLOREN_BEI_SO_VIELEN_FEHLERN
except ImportError:
    from tag14_loesung import VERLOREN_BEI_SO_VIELEN_FEHLERN


def ist_buchstabe(eingabe_von_nutzer: str) -> bool:
    if len(eingabe_von_nutzer) != 1:
        return False
    return True


def ist_aufgeben(eingabe_von_nutzer: str) -> bool:
    return eingabe_von_nutzer.lower() == "ich gebe auf"


def bewerte_geratenen_buchstaben(
    buchstabe: str,
    noch_gesuchte_buchstaben: Set[str],
    falsch_geratene_buchstaben: List[str]
    ) -> Optional[bool]:
    if buchstabe in noch_gesuchte_buchstaben:
        noch_gesuchte_buchstaben.remove(buchstabe)
        if len(noch_gesuchte_buchstaben) == 0:
            return "gewonnen"
        else:
            return "richtig-geraten"
    else:
        falsch_geratene_buchstaben.append(buchstabe)
        if len(falsch_geratene_buchstaben) >= VERLOREN_BEI_SO_VIELEN_FEHLERN:
            return "verloren"
        else:
            return "falsch-geraten"
