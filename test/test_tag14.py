from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from os.path import exists, abspath, dirname, join, pardir

try:
    from pyventskalender import tag14_loesung as heute
except ImportError:
    from pyventskalender import tag14 as heute


class Tag14Tests(TestCase):

    def test_datei_ist_da(self):
        erwarteter_dateipfad = abspath(join(dirname(__file__), pardir, "pyventskalender", "galgenmannbilder.py"))
        self.assertTrue(exists(erwarteter_dateipfad))

    def test_import_bilder(self):
        from pyventskalender import galgenmannbilder

    def test_galgenmannbild_exists(self):
        self.assertIn('galgenmannbild', dir(heute))

    def test_galgenmannbild(self):
        from pyventskalender.galgenmannbilder import HANGMANPICS
        for i in range(len(HANGMANPICS)):
            self.assertEqual(
                heute.galgenmannbild(i), HANGMANPICS[i], 
                msg="Bild für {} Fehler stimmt nicht".format(i))