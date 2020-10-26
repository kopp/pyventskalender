from unittest import TestCase 
from unittest.mock import patch

from pyventskalender import tag05_loesung as heute
ICH_TIPPE_AUF_PATH = "pyventskalender.tag05_loesung.ich_tippe_auf"
# Achtung: _loesung muss in import und _PATH identisch sein!

def make_ich_tippe_auf(fake_zufallszahl: int):
    def mock_ich_tippe_auf(zahl: int):
        if zahl > fake_zufallszahl:
            return "falsch, zu hoch"
        elif zahl < fake_zufallszahl:
            return "falsch, zu niedrig"
        else:
            return "richtig, gefunden!"
    return mock_ich_tippe_auf


class Tag05Tests(TestCase): 

    def test_finde_zufallszahl(self):
        for fake_zufallszahl in [10] + list(range(20)):
            with patch(
                ICH_TIPPE_AUF_PATH,
                side_effect=make_ich_tippe_auf(fake_zufallszahl),
            ):
                gefunden = heute.finde_zufallszahl()
                self.assertEqual(gefunden, fake_zufallszahl)
