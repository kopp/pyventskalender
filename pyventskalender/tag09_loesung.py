from typing import List, Union


def wie_viele_messungen_von(name: str, dateiname: str) -> int:
    vorkommnisse = 0
    with open(dateiname, "r") as datei:
        for zeile in datei:
            if name in zeile:
                vorkommnisse += 1
    return vorkommnisse


def durchschnitt(zahlen: List[Union[int, float]]) -> float:
    summe = 0
    for zahl in zahlen:
        summe += zahl
    anzahl = len(zahlen)
    return summe / anzahl