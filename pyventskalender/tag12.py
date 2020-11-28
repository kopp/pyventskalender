# Heute schauen wir uns an, wie man mit Fehlern umgeht: Exceptions.

# %%
# Wenn wir bspw. ein `dict`
adressbuch = {
    "Polizei": "112",
    "Paul": "07392 38945",
}
# haben, und "Peter" anrufen wollen, könnten wir zuerst nachschauen, ob ein
# Eintrag für "Peter" vorliegt:
"Peter" in adressbuch

# Was passiert aber, wenn wir das nicht testen, und einfach mal versuchen, die
# Nummer von "Peter" zu bekommen?
# Lade diese Zelle und probiere das mal im interaktiven Interpreter aus.
# %%
# Du dürftest einen `KeyError` gesehen haben -- eine Exception.
# Mit Exceptions gibt eine Funktion oder Methode an, dass hier etwas passiert
# ist, mit dem sie nicht umgehen kann.
# In diesem Fall wusste der `operator[]` (die Methode, die uns erlaubt
# `dict[key]` zu schreiben) nicht, was er machen soll, wenn der Schlüssel nicht
# vorhanden ist.
# Anstatt jetzt irgendwas zurück zu geben, sagt die Methode gleich klipp und
# klar, dass sie nicht weiter weiß.
#
# Um klar zu machen, dass es sich hier um einen Fehlerfall handelt (also dass
# die Methode gerade nichts ausgibt, sondern nicht richtig arbeiten kann),
# verwendet man für Exceptions `raise` statt `return`.
# Man spricht auf Deutsch davon, dass die Funktion "den Fehler XY wirft".
# Um dem menschlichen Leser einen Hinweis zu geben, was eigentlich das Problem
# ist, kann man den Exceptions eine Nachricht mitgeben; bspw.
#    raise ValueError("Negative Zahlen ergeben hier keinen Sinn")
#
# Die wichtigsten Exceptions sind
# - KeyError: Der Schlüssel ist nicht im Dictionary
# - IndexError: Wie KeyError nur für Listen
# - TypeError: Wenn eine Operation für einen Typ nicht unterstützt wird (bspw.
#   geteilt durch für zwei Strings: `"foo" / "bar"`)
# - ValueError: Wenn eine Operation für einen Wert nicht machbar ist, bspw. 
# Eine Liste von allen eingebauten Exceptions ist hier:
# https://docs.python.org/3/library/exceptions.html

# %% Input validieren -- Test 10
# Vervollständige jetzt die folgende Funktion, die das Volumen eines Würfels in
# Kubikmeter berechnen soll, wenn man ihr die Kantenlänge in Metern gibt.
# Die Funktion soll einen ValueError werfen, wenn eine negative Kantenlänge
# verwendet wird.

def volumen_wuerfel_mit_kantenlaenge(kantenlaenge: float) -> float:
    pass

# Was passiert, wenn du diese Funktion mit einem `str` als Argument aufrufst?

# %%
# Fehler passieren.
# Damit man trotz eines Fehlers weiterarbeiten kann, gibt es try-except-Blöcke.
# Dabei probiert man etwas aus (to `try` -- ausprobieren) und wenn das
# funktioniert ist alles gut.
# Wenn es dabei einen Fehler geben sollte, dann kann man diesen in einer
# Ausnahme behandeln (to `except` -- eine Ausnahme machen).
# Beispielsweise würde der folgende Code einfach mal probieren, ein Volumen zu
# berechnen, und wenn es nicht geht, eben ein anderes Volumen angeben.
try:
    volumen = volumen_wuerfel_mit_kantenlaenge(-1)
except ValueError:
    volumen = 0
except KeyError:
    print("Das soll nun wirklich nicht passieren!")

# Man kann mehrere `except`-Blöcke angeben, die auf verschiedene Fehler
# reagieren.
# %% Input validieren -- Test 20
# Vervollständige die Folgende Funktion, die eine Lise von Zahlen entgegen
# nimmt und eine Liste von Volumina damit berechnet.
# Sollte die Berechnung nicht funktionieren, soll der entsprechende Wert der
# Kantenlänge in einer zweiten Liste ausgegeben werden.
# Beispielsweise soll
#    viele_volumina_berechnen([1, 2, -3])
# den folgenden Output erzeugen:
#    ([1, 8], [-3])

from typing import Tuple, List

def viele_volumina_berechnen(kantenlaengen: List[float]) -> Tuple[List[float], List[float]]:
    pass