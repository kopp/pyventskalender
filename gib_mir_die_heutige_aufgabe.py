from datetime import date
from argparse import ArgumentParser
from urllib.request import urlopen
from os.path import join, abspath, dirname, exists
from os import makedirs
from typing import List
from re import compile
from json import loads
from subprocess import run
from sys import executable
from traceback import format_exc


GITHUB_RAW_BASE_PATH = "https://raw.githubusercontent.com/kopp/pyventskalender/master/"
ZUSAETZLICH_HERUNTERLADEN_JSON = "pyventskalender.zusaetzlich-herunterladen.json"
# Format:
# {
#   "<tag-nummer>": [
#                      { "url": "<url>", "lokal": "<pfad>", "ausfuehren": "<bool>" }
#                   ]
# }
LOCAL_BASE_PATH = abspath(dirname(__file__))
VERWEIS_AUF_WEITERE_DATEIEN_RE = compile(r"^# Setzt Datei (.+) voraus.$")


def hole_aktuellen_tag_im_advent() -> int:
    heute = date.today()
    if heute.month != 12:
        raise ValueError("Advent ist nur im Dezember")
    if heute.day > 24:
        raise ValueError("Advent geht nur bis 24. Dezember")
    return heute.day


def _stelle_sicher_dass_ordner_existiert_fuer(absoluter_dateipfad: str):
    ordner = dirname(absoluter_dateipfad)
    if not exists(ordner):
        makedirs(ordner, exist_ok=True)


def _lade_datei_aus_internet(url: str, dateipfad: str, ueberschreiben: bool = False):
    antwort = urlopen(url)
    inhalt = antwort.read()
    lokaler_pfad = join(LOCAL_BASE_PATH, dateipfad)
    modus_zum_schreiben = "w" if ueberschreiben else "x"
    _stelle_sicher_dass_ordner_existiert_fuer(lokaler_pfad)
    with open(lokaler_pfad, modus_zum_schreiben, encoding="utf-8") as lokale_datei:
        lokale_datei.write(inhalt.decode("utf-8"))


def _lade_datei_von_github(dateipfad: str, ueberschreiben: bool = False):
    url = GITHUB_RAW_BASE_PATH + dateipfad
    _lade_datei_aus_internet(url, dateipfad, ueberschreiben)


def _suche_weitere_abhaengige_dateien_in(dateipfad: str) -> List[str]:
    abhaengige_dateien = []
    with open(dateipfad, "r") as datei:
        for zeile in datei:
            uebereinstimmung = VERWEIS_AUF_WEITERE_DATEIEN_RE.match(zeile)
            if uebereinstimmung:
                verwiesene_datei = uebereinstimmung.group(1)
                abhaengige_dateien.append(verwiesene_datei)
    return abhaengige_dateien


def _versuche_datei_von_github_zu_laden(dateipfad: str, ueberschreiben=True):
    try:
        _lade_datei_von_github(dateipfad, ueberschreiben)
    except:  # noqa
        print("Fehler beim Herunterladen von {} -- bitte nochmal versuchen"
              " oder kompetente Hilfe holen.".format(dateipfad))


def _lade_zusaetzliche_dateien_herunter(
        tag: int,
        url: str = GITHUB_RAW_BASE_PATH + ZUSAETZLICH_HERUNTERLADEN_JSON,
        ):
    try:
        antwort = urlopen(url)
        inhalt = loads(antwort.read())
    except:  # noqa
        print("Fehler beim Herunterladen zusätzlicher Dateien -- bitte"
              " professionelle Hilfe holen.  Fehler {}".format(format_exc()))
        return
    if str(tag) in inhalt:
        for datei in inhalt[str(tag)]:
            try:
                _lade_datei_aus_internet(
                        datei["url"],
                        datei["lokal"],
                        True
                )
                if datei["ausfuehren"]:
                    run([executable, datei["lokal"]])
            except:  # noqa
                print("Fehler beim Herunterladen von {} von {} -- bitte"
                      " professionelle Hilfe holen.  Fehler {}".format(
                          datei["lokal"],
                          datei["url"],
                          format_exc(),
                      ))


def _lade_vorausgegangenen_tag_falls_notwendig(aktueller_tag: int):
    if aktueller_tag > 1:
        gestriger_tag = aktueller_tag - 1
        datei_von_gestern = "pyventskalender/tag{:02d}.py".format(gestriger_tag)
        if not exists(datei_von_gestern):
            print(f"Die Dateien von gestern (Tag {gestriger_tag}) wurden nicht gefunden")
            aktualisiere_problem_tag(gestriger_tag)


def aktualisiere_problem_tag(tag: int) -> None:
    _lade_vorausgegangenen_tag_falls_notwendig(tag)
    print("Aktualisiere auf Tag {}".format(tag))
    datei_des_tages = "pyventskalender/tag{:02d}.py".format(tag)
    neue_dateien = [
            datei_des_tages,
            "test/test_tag{:02d}.py".format(tag),
            ]
    test_von_gestern = None
    if tag > 1:
        neue_dateien.append("pyventskalender/tag{:02d}_loesung.py".format(tag - 1))
        test_von_gestern = "test/test_tag{:02d}.py".format(tag - 1)
    else:
        neue_dateien.append("pyventskalender/__init__.py")
        neue_dateien.append("test/__init__.py")
    # lade es herunter
    _lade_zusaetzliche_dateien_herunter(tag)
    if test_von_gestern is not None:
        # Geaendert: in test_tag{tag-1} wird aus tag{tag-1} -> tag{tag-1}_loesung
        # Die Datei muss also ueberschrieben werden.
        _versuche_datei_von_github_zu_laden(test_von_gestern, True)
    for datei in neue_dateien:
        _versuche_datei_von_github_zu_laden(datei)
        for abhaengige_datei in _suche_weitere_abhaengige_dateien_in(datei):
            _versuche_datei_von_github_zu_laden(abhaengige_datei)


def _verarbeite_kommandozeilenparameter() -> int:
    parser = ArgumentParser("Aktualisiere auf die Aufgabe von einem bestimmten Tag.")
    parser.add_argument("--tag",
                        type=int,
                        help="Wähle diesen Tag im Advent",
                        default=None,
                        )
    args = parser.parse_args()

    if args.tag is None:
        tag = hole_aktuellen_tag_im_advent()
    else:
        tag = args.tag

    return tag


if __name__ == "__main__":
    try:
        tag = _verarbeite_kommandozeilenparameter()
        aktualisiere_problem_tag(tag)
    except ValueError:
        print("Sicher, dass es grade Advent ist?")
        print("Lass das Programm mit --help laufen, um mehr zu sehen.")
