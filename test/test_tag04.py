from unittest import TestCase 

from pyventskalender import tag04_loesung as heute


class Tag04Tests(TestCase): 
      
    def test_ich_haette_gerne_so_viele_katzen(self):
        self.assertEqual(
            heute.ich_haette_gerne_so_viele_katzen(1),
            "Ich hätte gerne 1 Katze",
        )
        self.assertEqual(
            heute.ich_haette_gerne_so_viele_katzen(4),
            "Ich hätte gerne 4 Katzen",
        )

    def test_ich_tippe_auf(self):
        heute.zufallszahl = 5
        self.assertEqual(heute.ich_tippe_auf(4), "falsch, zu niedrig")
        self.assertEqual(heute.ich_tippe_auf(5), "richtig, gefunden!")
        self.assertEqual(heute.ich_tippe_auf(6), "falsch, zu hoch")