from typing import Tuple, List

def volumen_wuerfel_mit_kantenlaenge(kantenlaenge: float) -> float:
    if kantenlaenge < 0:
        raise ValueError("Negative Kantenlängen ergeben keinen Sinn.")
    else:
        return kantenlaenge * kantenlaenge * kantenlaenge


def viele_volumina_berechnen(kantenlaengen: List[float]) -> Tuple[List[float], List[float]]:
    volumina = []
    kantenlaengen_mit_fehlern = []
    for kantenlaenge in kantenlaengen:
        try:
            volumen = volumen_wuerfel_mit_kantenlaenge(kantenlaenge)
            volumina.append(volumen)
        except ValueError:
            kantenlaengen_mit_fehlern.append(kantenlaenge)
    return volumina, kantenlaengen_mit_fehlern
