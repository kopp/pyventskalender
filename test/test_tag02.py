from unittest import TestCase 
from pyventskalender.tag02_loesung import (
    elchgeraeusch, katzengeraeusch, addiere, zaehle_tierlaute,
    subtrahiere_elchrufe_von_katzenrufen,
)
  
class Tag02Tests(TestCase): 
      
    def test_anzahl_mooos(self): 
        expected = "Mööö Mööö "
        self.assertEqual(elchgeraeusch(2), expected)

    def test_anzahl_miaus(self):
        expected = "Miau Miau "
        self.assertEqual(katzengeraeusch(2), expected)

    def test_addiere(self):
        self.assertEqual(addiere(2, 5), 2 * "Mööö " + 5 * "Miau ")
        self.assertEqual(addiere(3, 1), 3 * "Mööö " + 1 * "Miau ")
        self.assertEqual(addiere(1, 0), "Mööö ")
        self.assertEqual(addiere(0, 1), "Miau ")

    def test_zaehle_tierlaute(self):
        self.assertEqual(zaehle_tierlaute("Mööö Miau Mööö Miau "), 4)
        self.assertEqual(zaehle_tierlaute(""), 0)

    def test_subtrahiere_elchrufe_von_katzenrufen(self):
        self.assertEqual(subtrahiere_elchrufe_von_katzenrufen(
            "Mööö Mööö Mööö ", "Miau Miau "), "Mööö ")
        self.assertEqual(subtrahiere_elchrufe_von_katzenrufen(
            "Mööö ", "Miau "), "")
        # Wir testen nicht, ob da wirklich ein Elch oder eine Katze ruft
        self.assertEqual(subtrahiere_elchrufe_von_katzenrufen(
            "Mööö Mööö", "Mööö "), "Mööö ")
