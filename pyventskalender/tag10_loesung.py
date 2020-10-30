from typing import List, Union
import re

GEWICHT_RE = re.compile(r"(\d+)\.(\d+). (.+) wiegt (\d+)kg")


def extrahiere_gewichte(dateiname: str) -> List[List[str]]:
    gewichte = []
    with open(dateiname, "r") as datei:
        for zeile in datei:
            gefunden = GEWICHT_RE.match(zeile)
            if gefunden:
                name = gefunden.group(3)
                gewicht = gefunden.group(4)
                daten_dieser_zeile = [name, gewicht]
                gewichte.append(daten_dieser_zeile)
    return gewichte


def gewichte_als_zahlen(gewichte: List[List[str]]) -> List[List[Union[str, float]]]:
    ausgabe = []
    for name_gewicht in gewichte:
        name = name_gewicht[0]
        gewicht = float(name_gewicht[1])
        ausgabe.append([name, gewicht])
    return ausgabe
