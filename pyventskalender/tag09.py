# Ein beliebtes Problem, das man mit Python lösen kann, ist, eine Textdatei zu
# durchsuchen und daraus Daten zu generieren.
# Hier wollen wir uns die Datei `beispieldaten_gewichte.txt` anschauen.
# Sie enthält ein Gewicht pro Tag.

# %%
# Eine Datei wird mit `open` geöffnet.
# Hinweis: Das "r" steht für _read_, `datei` ist das Objekt, das den Inhalt der
# Datei repräsentiert.
# Man kann die Funktion verwenden per `datei_ausgeben("beispieldaten_gewichte.txt")`

def datei_ausgeben(dateiname):
    with open(dateiname, "r") as datei:
        for zeile in datei:
            print(zeile)

# %%
# Vervollständige die Funktion so, dass sie ausgibt, wie viele Messungen es in
# der betreffenden Datei für einen bestimmten Namen gibt.

def wie_viele_messungen_von(name: str, dateiname: str) -> int:
    pass


# %%
# Solltest du Hilfe brauchen, dann führe diese Funktion aus:
def hilfe_wie_viele_messungen_von():
    import base64
    print(
        base64.b64decode(
            b'RHUga2FubnN0IHBlciBgImZvbyIgaW4gImFzZGYgZm9vIGJhciJgIHBydWVmZW4sIG9iIGRlciBzdHJpbmcgImZvbyIgaW4gImFzZGYgZm9vIGJhciIgdm9ya29tbXQ='
        ).decode()
    )

# %%
# Grade bei Gewicht, das täglich schwankt, ist es interessant, einen
# Durchschnitt zu bilden.
# Vervollständige deshalb die folgende Funktion, die einen Durchschnitt aus
# einer Liste von Zahlen bildet.

from typing import List, Union

def durchschnitt(zahlen: List[Union[int, float]]) -> float:
    pass

# Hinweis: `Union[int, float]`` bedeutet, dass ein Objekt entweder ein `int`
# oder ein `float` ist.
