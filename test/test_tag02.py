from unittest import TestCase
try:
    from pyventskalender import tag02_loesung as heute
except ImportError:
    from pyventskalender import tag02 as heute


class Tag02Tests(TestCase):

    def test_anzahl_mooos(self):
        expected = "Mööö Mööö "
        self.assertEqual(heute.elchgeraeusch(2), expected)

    def test_anzahl_miaus(self):
        expected = "Miau Miau "
        self.assertEqual(heute.katzengeraeusch(2), expected)

    def test_addiere(self):
        self.assertEqual(heute.addiere(2, 5), 2 * "Mööö " + 5 * "Miau ")
        self.assertEqual(heute.addiere(3, 1), 3 * "Mööö " + 1 * "Miau ")
        self.assertEqual(heute.addiere(1, 0), "Mööö ")
        self.assertEqual(heute.addiere(0, 1), "Miau ")

    def test_zaehle_tierlaute(self):
        self.assertEqual(heute.zaehle_tierlaute("Mööö Miau Mööö Miau "), 4)
        self.assertEqual(heute.zaehle_tierlaute(""), 0)

    def test_subtrahiere_elchrufe_von_katzenrufen(self):
        self.assertEqual(heute.subtrahiere_elchrufe_von_katzenrufen(
            "Mööö Mööö Mööö ", "Miau Miau "), "Mööö ")
        self.assertEqual(heute.subtrahiere_elchrufe_von_katzenrufen(
            "Mööö ", "Miau "), "")
        # Wir testen nicht, ob da wirklich ein Elch oder eine Katze ruft
        self.assertEqual(heute.subtrahiere_elchrufe_von_katzenrufen(
            "Mööö Mööö", "Mööö "), "Mööö ")
