from unittest import defaultTestLoader, TextTestRunner, TextTestResult, TestCase
from os import path, walk, stat, devnull
from json import loads
from typing import List, Tuple
from random import seed, choices
from inspect import getsourcelines


PROJECT_TOPLEVEL_DIR = path.dirname(path.realpath(__file__))
PROJECT_STANDARD_KONFIGURATION_DATEI = "pyventskalender.default-config.json"
PROJECT_ANGEPASSTE_KONFIGURATION_DATEI = "pyventskalender.config.json"
PROJECT_CODE_DIR = "pyventskalender"


def ignoriere(*argumente):
    pass


def lasse_unit_tests_laufen() -> TextTestResult:
    gefundene_tests = defaultTestLoader.discover(
        start_dir=path.join(PROJECT_TOPLEVEL_DIR, "test"),
        top_level_dir=PROJECT_TOPLEVEL_DIR,
    )
    test_ausfuehrer = TextTestRunner(stream=open(devnull, "w"))
    test_resultate = test_ausfuehrer.run(gefundene_tests)
    return test_resultate


def _lade_konfiguration():
    json_konfigurationsdatei = path.join(
        PROJECT_TOPLEVEL_DIR, PROJECT_ANGEPASSTE_KONFIGURATION_DATEI)
    if not path.exists(json_konfigurationsdatei):
        # Keine Angepasste Konfiguration gefunden; Standard wird verwendet
        json_konfigurationsdatei = path.join(
            PROJECT_TOPLEVEL_DIR, PROJECT_STANDARD_KONFIGURATION_DATEI)
    with open(json_konfigurationsdatei, "r") as dateihandle:
        dateiinhalt = dateihandle.read()
        konfiguration = loads(dateiinhalt)
    return konfiguration


def _finde_belohnungen() -> Tuple[List["str"], List[int]]:
    """
    Liefert zwei listen: Belohnungen und jeweilige relative Gewichte.
    """
    konfiguration = _lade_konfiguration()
    belohnungen = []
    gewichte = []
    for belohnung in konfiguration["Belohnungen"]:
        belohnungen.append(belohnung["Name"])
        gewichte.append(belohnung["Gewichtung"])
    return belohnungen, gewichte


def _bestimme_dateigroesse_python_files_in_bytes(pfad):
    dateigroesse_summe = 0
    for ordner, _, dateien in walk(pfad):
        for datei in dateien:
            if datei.endswith(".py"):
                kompletter_pfad_zu_datei = path.join(ordner, datei)
                dateigroesse_summe += stat(kompletter_pfad_zu_datei).st_size
    return dateigroesse_summe


def bestimme_belohnung():
    seed(_bestimme_dateigroesse_python_files_in_bytes(
        path.join(PROJECT_TOPLEVEL_DIR, PROJECT_CODE_DIR)))
    belohnungen, gewichte = _finde_belohnungen()
    wahl = choices(belohnungen, gewichte)[0]
    return wahl


def _sortiere_ergebnisse_nach_zeilennummer_der_testfunktion(ergebnisse):

    def zeilennummer_von_test(fehler: TestCase) -> int:
        methode = getattr(fehler, fehler._testMethodName)
        text, linenumber = getsourcelines(methode)
        ignoriere(text)
        return linenumber

    def zeilennummer_von_ergebnis(ergebnis):
        fehler, backtrace = ergebnis
        ignoriere(backtrace)
        return zeilennummer_von_test(fehler)

    ergebnisse_sortiert = sorted(ergebnisse, key=zeilennummer_von_ergebnis)
    return ergebnisse_sortiert


def belohnung_wenn_unittests_ok():
    unit_test_ergebnisse = lasse_unit_tests_laufen()
    alle_unit_tests_sind_ok = unit_test_ergebnisse.wasSuccessful()
    if alle_unit_tests_sind_ok:
        print("Ja, das sieht gut aus -- Belohnung ist verdient :-)")
        belohnung = bestimme_belohnung()
        print("Deine Belohnung heute: {}".format(belohnung))
    else:
        print("Leider scheinen noch nicht alle Tests zu funktionieren.")
        print("Hier folgt eine Liste von Tests, die noch fehlschlagen:")
        fehlschlaege = unit_test_ergebnisse.errors + unit_test_ergebnisse.failures
        fehlschlaege_sortiert_nach_reihenfolge_in_datei = _sortiere_ergebnisse_nach_zeilennummer_der_testfunktion(fehlschlaege)
        for fehler, traceback in fehlschlaege_sortiert_nach_reihenfolge_in_datei:
            print("\n")
            print("--> Fehlschlag in Test {}:".format(str(fehler)))
            print(traceback)
        print("\n")
        print("Bitte versuche es weiter.")
        print("Viel Erfolg!")


if __name__ == "__main__":
    belohnung_wenn_unittests_ok()
