from unittest import TestCase
from unittest.mock import patch

try:
    from pyventskalender import tag15_loesung as heute
except ImportError:
    from pyventskalender import tag15 as heute


class Tag15Tests(TestCase):

    def test_ist_buchstabe_vorhanden(self):
        self.assertIn("ist_buchstabe", dir(heute),
                      msg="ist_buchstabe ist noch nicht definiert (oder falsch geschrieben)")

    def test_ist_buchstabe_annotations(self):
        self.assertEqual(len(heute.ist_buchstabe.__annotations__), 2,
                         msg="Bitte annotiere den Typ des Arguments und des Rückgabewerts.")
        self.assertEqual(
            set(heute.ist_buchstabe.__annotations__.values()),
            set([str, bool]),
            msg="Die Typen sollten str für den Input und bool für den Rückgabewert sein."
        )

    def test_ist_buchstabe(self):
        for buchstabe in ["a", "A", "1", " ", "ä", "Ä", "ß"]:
            self.assertTrue(heute.ist_buchstabe(buchstabe))
        for eingabe in ["aa", "a ", "AA", "aaaa", ""]:
            self.assertFalse(heute.ist_buchstabe(eingabe))

    def test_ist_aufgeben_vorhanden(self):
        self.assertIn("ist_aufgeben", dir(heute),
                      msg="ist_aufgeben ist noch nicht definiert (oder falsch geschrieben)")

    def test_ist_aufgeben(self):
        for aufgabe in ["ich gebe auf", "Ich Gebe Auf", "ICH GEBE AUF"]:
            self.assertTrue(heute.ist_aufgeben(aufgabe))
        for falsche_aufgabe in ["Ich gebe auf.", "Aufgabe", "asdf"]:
            self.assertFalse(heute.ist_aufgeben(falsche_aufgabe))

    def test_bewerte_geratenen_buchstaben(self):
        noch_gesucht = set("ab")
        falsch_geraten = []

        bewertung = heute.bewerte_geratenen_buchstaben("x", noch_gesucht, falsch_geraten)
        self.assertEqual(bewertung, "falsch-geraten")
        self.assertEqual(noch_gesucht, set("ab"))
        self.assertEqual(falsch_geraten, ["x"])

        bewertung = heute.bewerte_geratenen_buchstaben("a", noch_gesucht, falsch_geraten)
        self.assertEqual(bewertung, "richtig-geraten")
        self.assertEqual(noch_gesucht, set("b"))
        self.assertEqual(falsch_geraten, ["x"])

        bewertung = heute.bewerte_geratenen_buchstaben("y", noch_gesucht, falsch_geraten)
        self.assertEqual(bewertung, "falsch-geraten")
        self.assertEqual(noch_gesucht, set("b"))
        self.assertEqual(falsch_geraten, ["x", "y"])

        bewertung = heute.bewerte_geratenen_buchstaben("y", noch_gesucht, falsch_geraten)
        self.assertEqual(bewertung, "falsch-geraten")
        self.assertEqual(noch_gesucht, set("b"))
        self.assertEqual(falsch_geraten, ["x", "y", "y"])

        bewertung = heute.bewerte_geratenen_buchstaben("b", noch_gesucht, falsch_geraten)
        self.assertEqual(bewertung, "gewonnen")
        self.assertEqual(noch_gesucht, set())
        self.assertEqual(falsch_geraten, ["x", "y", "y"])

    def test_bewerte_geratenen_buchstaben_verloren(self):
        noch_gesucht = set("ab")
        falsch_geraten = []

        for i in range(1, heute.VERLOREN_BEI_SO_VIELEN_FEHLERN):
            bewertung = heute.bewerte_geratenen_buchstaben("x", noch_gesucht, falsch_geraten)
            self.assertEqual(bewertung, "falsch-geraten")
            self.assertEqual(noch_gesucht, set("ab"))
            self.assertEqual(falsch_geraten, i * ["x"])

        bewertung = heute.bewerte_geratenen_buchstaben("x", noch_gesucht, falsch_geraten)
        self.assertEqual(noch_gesucht, set("ab"))
        self.assertEqual(falsch_geraten, heute.VERLOREN_BEI_SO_VIELEN_FEHLERN * ["x"])
        self.assertEqual(bewertung, "verloren")
