# Neben der `while`-Schleife, die Code so lange ausgeführt hatte, wie eine
# bestimmte Bedingung wahr war, gibt es die `for`-Schleife, die den selben Code
# für jedes Objekt einer Menge von Objekten ausführt.
# Im einfachsten Fall kann man sich per `range(10)` eine Menge von 10 Zahlen
# erzeugen lassen -- und zwar die Zahlen 0, 1, ..., 9.

# %%
# Damit kann man so etwas schreiben wie

def kuh_sinnspruch_beispiel():
    for anzahl_muhs in range(10):
        print("{} Kühe machen {} mal Mühe".format(anzahl_muhs, anzahl_muhs))
# %% Einfaches for -- Test 10
# Das ist sprachlich noch nicht ganz sicher.
# Um die Ausgabe zu verbessern, vervollständige die folgende Funktion so, dass sie
# - bei 0 Kühen "0 Kühe machen keine Mühe"
# - bei 1 Kuh "1 Kuh macht Muh"
# - bei mehreren Kühen den Text wie oben, also bspw.
#   bei 4 Kühen "4 Kühe machen 4 mal Mühe"

def kuehe_machen_muehe(anzahl: int) -> str:
    pass

# %% Weiteres for -- Test 20
# Und jetzt vervollständige die folgende Funktion, damit sie eine Liste von
# solchen sinnhaften Sprüchen ausgibt und zwar für alle Kuh-Anzahlen zwischen
# zwei Zahlen.
# Mit "ausgeben" ist hier `print` gemeint.
#
# Hinweis: `range(5, 10)` erzeugt die Zahlen 5, 6, ..., 9
# Hinweis: die zu vervollständigende Funktion hat eine andere Konvention!
# Hinweis: Der Rückgabetyp `None` bedeutet, dass die Funktion nichts
#          zurückgibt, also kein `return` verwendet. Alle Ausgaben, die sie macht,
#          passieren per `print`.

def kuh_sinnsprueche(anzahl_min: int, anzahl_max: int) -> None:
    """
    Gib den Sinnspruch der Funktion `kuehe_machen_muehe` für alle
    Kuh-Anzahlen zwischen `anzahl_min` und `anzahl_max` aus.
    (Also bei anzahl_min=5 und anzahl_max=7 wird der Text für 5, 6, und 7
    ausgegeben.)
    """
    pass
