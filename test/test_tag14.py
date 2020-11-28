from unittest import TestCase
from os.path import exists, abspath, dirname, join, pardir

try:
    from pyventskalender import tag14_loesung as heute
except ImportError:
    from pyventskalender import tag14 as heute


class Tag14Tests(TestCase):

    def test_10_datei_ist_da(self):
        erwarteter_dateipfad = abspath(join(dirname(__file__), pardir, "pyventskalender", "galgenmannbilder.py"))
        self.assertTrue(exists(erwarteter_dateipfad),
                        msg=f"Datei {erwarteter_dateipfad} existiert nicht.")

    def test_20_import_file(self):
        from pyventskalender import galgenmannbilder

    def test_30_import_bilder(self):
        from pyventskalender.galgenmannbilder import HANGMANPICS

    def test_40_galgenmannbild_exists(self):
        self.assertIn('galgenmannbild', dir(heute))

    def test_50_galgenmannbild(self):
        from pyventskalender.galgenmannbilder import HANGMANPICS
        for i in range(len(HANGMANPICS)):
            self.assertEqual(
                heute.galgenmannbild(i), HANGMANPICS[i], 
                msg="Bild für {} Fehler stimmt nicht".format(i))

    def test_60_maximale_fehler_existiert(self):
        self.assertIn("VERLOREN_BEI_SO_VIELEN_FEHLERN", dir(heute))

    def test_70_maximale_fehler_wert(self):
        from pyventskalender.galgenmannbilder import HANGMANPICS
        self.assertEqual(heute.VERLOREN_BEI_SO_VIELEN_FEHLERN, len(HANGMANPICS) - 1)

    def test_80_zu_ratendes_wort(self):
        self.assertEqual(heute.zu_ratendes_wort("heute", set("heute")), "_____",
                         msg="Wenn noch alles erraten werden soll, muss _____ rauskommen")
        self.assertEqual(heute.zu_ratendes_wort("heute", set("h")), "_eute")
        self.assertEqual(heute.zu_ratendes_wort("heute", set("e")), "h_ut_",
                         msg="Ein Buchstabe kann mehrmals vorkommen")
        self.assertEqual(heute.zu_ratendes_wort("heute", set("hte")), "__u__")
        self.assertEqual(heute.zu_ratendes_wort("heute", []), "heute",
                         msg="Wenn nichts mehr zu erraten ist, dann gib das Wort aus")
        self.assertEqual(heute.zu_ratendes_wort("Heute", set("heute")), "_____",
                         msg="Das Wort kann Groß- und Kleinbuchstaben enthalten, die zu erratenden Buchstaben sind alle klein.")
        self.assertEqual(heute.zu_ratendes_wort("süß", set("üß")), "s__",
                         msg="Das Wort kann Umlaute und ß enthalten")

