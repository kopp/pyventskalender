from unittest import TestCase 
from unittest.mock import patch, mock_open

from pyventskalender import tag09_loesung as heute


class Tag09Tests(TestCase): 

    def test_wie_viele_messungen_von(self):
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
            self.assertEqual(
                heute.wie_viele_messungen_von("Herrmann", "fake.txt"),
                3)
            self.assertEqual(
                heute.wie_viele_messungen_von("Caro", "fake.txt"),
                5)
            self.assertEqual(
                heute.wie_viele_messungen_von("Paul", "fake.txt"),
                2)
            self.assertEqual(
                heute.wie_viele_messungen_von("Romeo", "fake.txt"),
                0)

    def test_durchschnitt(self):
        self.assertAlmostEqual(heute.durchschnitt([1]), 1)
        self.assertAlmostEqual(heute.durchschnitt([5] * 10), 5)
        self.assertAlmostEqual(heute.durchschnitt([1, 2, 3]), 2)
        self.assertAlmostEqual(
            heute.durchschnitt(list(range(51))),
            25,
        )
        
