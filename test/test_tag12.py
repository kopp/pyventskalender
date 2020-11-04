from unittest import TestCase

try:
    from pyventskalender import tag12_loesung as heute
except ImportError:
    from pyventskalender import tag12 as heute


class Tag12Tests(TestCase):

    def test_volumen_wuerfel_mit_kantenlaenge(self):
        self.assertAlmostEqual(heute.volumen_wuerfel_mit_kantenlaenge(1), 1)
        self.assertAlmostEqual(heute.volumen_wuerfel_mit_kantenlaenge(2), 8)
        self.assertAlmostEqual(heute.volumen_wuerfel_mit_kantenlaenge(0), 0)
        with self.assertRaises(ValueError):
            heute.volumen_wuerfel_mit_kantenlaenge(-1)

    def test_viele_volumina_berechnen(self):
        self.assertEqual(heute.viele_volumina_berechnen([]), ([], []))
        self.assertEqual(heute.viele_volumina_berechnen([1, 2]), ([1, 8], []))
        self.assertEqual(heute.viele_volumina_berechnen([2]), ([8], []))
        self.assertEqual(heute.viele_volumina_berechnen([-2]), ([], [-2]))
        self.assertEqual(heute.viele_volumina_berechnen([2, -2]), ([8], [-2]))