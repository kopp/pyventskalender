from unittest import TestCase
from unittest.mock import patch, mock_open

try:
    from pyventskalender import tag10_loesung as heute
except ImportError:
    from pyventskalender import tag10 as heute


class Tag10Tests(TestCase):

    def test_10_extrahiere_gewichte(self):
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
            self.assertEqual(len(gewichte), 10)
            self.assertEqual(gewichte[0], ["Herrmann", "72"])
            self.assertEqual(gewichte[1], ["Caro", "62"])
            self.assertEqual(gewichte[2], ["Paul", "32"])

    def test_20_gewichte_als_zahlen(self):
        pseudo_data = [["x", "1"], ["y", "2"]]
        output = heute.gewichte_als_zahlen(pseudo_data)
        self.assertEqual(output[0][1], 1)
        self.assertEqual(output[1][1], 2)
