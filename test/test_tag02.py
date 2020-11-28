from unittest import TestCase
from inspect import signature
try:
    from pyventskalender import tag02_loesung as heute
except ImportError:
    from pyventskalender import tag02 as heute


class Tag02Tests(TestCase):

    def test_10_katzengeraeusch_parameter(self):
        signatur_von_katzengeraeusch = signature(heute.katzengeraeusch)
        anzahl_parameter = len(signatur_von_katzengeraeusch.parameters)
        self.assertEqual(anzahl_parameter, 1,
                         msg="katzengeraeusch sollte genau einen Paramerer entgegennehmen.")

    def test_20_anzahl_miaus(self):
        self.assertEqual(heute.katzengeraeusch(1), "Miau ")
        self.assertEqual(heute.katzengeraeusch(2), "Miau Miau ")
        self.assertEqual(heute.katzengeraeusch(3), "Miau Miau Miau ")

    def test_30_addiere(self):
        self.assertEqual(heute.addiere(2, 5), 2 * "Mööö " + 5 * "Miau ")
        self.assertEqual(heute.addiere(3, 1), 3 * "Mööö " + 1 * "Miau ")
        self.assertEqual(heute.addiere(1, 0), "Mööö ")
        self.assertEqual(heute.addiere(0, 1), "Miau ")

    def test_40_zaehle_tierlaute(self):
        self.assertEqual(heute.zaehle_tierlaute("Mööö Miau Mööö Miau "), 4)
        self.assertEqual(heute.zaehle_tierlaute(""), 0)

    def test_50_subtrahiere_elchrufe_von_katzenrufen(self):
        self.assertEqual(heute.subtrahiere_elchrufe_von_katzenrufen(
            "Mööö Mööö Mööö ", "Miau Miau "), "Mööö ")
        self.assertEqual(heute.subtrahiere_elchrufe_von_katzenrufen(
            "Mööö ", "Miau "), "")
        # Wir testen nicht, ob da wirklich ein Elch oder eine Katze ruft
        self.assertEqual(heute.subtrahiere_elchrufe_von_katzenrufen(
            "Mööö Mööö", "Mööö "), "Mööö ")
