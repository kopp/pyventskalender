from unittest import TestCase
from unittest.mock import patch, mock_open

try:
    from pyventskalender import tag11_loesung as heute
except ImportError:
    from pyventskalender import tag11 as heute


class Tag11Tests(TestCase):

    def test_10_adressbuch(self):
        self.assertIn("Wolfgang", heute.adressbuch)
        self.assertEqual(type(heute.adressbuch["Wolfgang"]), list)
        self.assertEqual(
            heute.adressbuch["Wolfgang"],
            ["0176 84927413", "07421 39495"],
        )

    def test_20_extrahiere_gewichte(self):
        pseudo_file = mock_open(read_data="""
1.11. Herrmann wiegt 72kg
1.11. Caro wiegt 62kg
1.11. Paul wiegt 32kg
2.11. Herrmann wiegt 73kg
2.11. Caro wiegt 60kg
3.11. Herrmann wiegt 71kg
3.11. Caro wiegt 59kg
3.11. Paul wiegt 32kg
4.11. Caro wiegt 60kg
6.11. Caro wiegt 60kg
        """)
        with patch('builtins.open', pseudo_file):
            gewichte = heute.extrahiere_gewichte("fake.txt")
            self.assertEqual(type(gewichte), dict)
            self.assertIn("Herrmann", gewichte)
            self.assertIn("Paul", gewichte)
            self.assertIn("Caro", gewichte)
            for name in ["Herrmann", "Paul", "Caro"]:
                self.assertEqual(type(gewichte[name]), list)
                for gewicht in gewichte[name]:
                    self.assertEqual(type(gewicht), int)
            self.assertEqual(len(gewichte["Herrmann"]), 3)
            self.assertEqual(len(gewichte["Paul"]), 2)
            self.assertEqual(len(gewichte["Caro"]), 5)
