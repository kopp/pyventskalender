from typing import Dict, List
import re

adressbuch = {
    "Feuerwehr": "110",
    "Polizei": "112",
    "Herrmann": "07543 73135",
    "Caro": "07314 93849193",
}

adressbuch["Caro"] = "07314 4815"
adressbuch["Paul"] = "07321 37294"

adressbuch["Wolfgang"] = ["0176 84927413", "07421 39495"]


GEWICHT_RE = re.compile(r"(\d+)\.(\d+). (.+) wiegt (\d+)kg")

def extrahiere_gewichte(dateiname: str) -> Dict[str, List[int]]:
    gewichte = {}
    with open(dateiname, "r") as datei:
        for zeile in datei:
            gefunden = GEWICHT_RE.match(zeile)
            if gefunden:
                name = gefunden.group(3)
                gewicht = int(gefunden.group(4))
                if name not in gewichte:
                    gewichte[name] = []
                gewichte[name].append(gewicht)
    return gewichte