from unittest import TestCase
from unittest.mock import MagicMock
from os.path import exists, pardir, join, abspath, dirname
from os import environ

PROJEKT_ORDNER = abspath(join(dirname(__file__), pardir))
VENV_ORDNER = join(PROJEKT_ORDNER, "venv")

try:
    from pyventskalender import tag21_loesung as heute

    class Tag21ArcadeTests(TestCase):
        pass

except ImportError:
    from pyventskalender import tag21 as heute

    class Tag21ArcadeTests(TestCase):

        def test_10_venv_ordner_existiert(self):
            self.assertTrue(exists(VENV_ORDNER),
                            msg=f"venv Ordner existiert noch nicht; erwartet bei {VENV_ORDNER}")
            
        def test_20_virtual_env_aktiviert(self):
            aktives_virtual_environment = environ.get("VIRTUAL_ENV")
            self.assertIsNotNone(aktives_virtual_environment,
                                msg="Das Virtual env scheint nicht aktiviert zu sein")
            self.assertEqual(VENV_ORDNER, aktives_virtual_environment,
            msg=f"Das aktivierte Virtual Environment ist nicht an der erwarteten Stelle {VENV_ORDNER}")

        def test_30_arcade_installiert(self):
            try:
                import arcade
                import_funtioniert = True
            except ModuleNotFoundError:
                import_funtioniert = False
            self.assertTrue(import_funtioniert,
                            msg="Es war nicht möglich, arcade zu importieren.  Hast du es installiert?")

try:
    import arcade
except ImportError:
    print("Fehler beim importieren von 'arcade'.  Bitte installiere arcade und aktiviere das venv in das du es installiert hast.")

class Tag21Tests(TestCase):

    def test_40_spieler_ist_angelegt(self):
        fenster = heute.FindeDenSchnellstenWeg(600, 600)
        self.assertIn("spieler", dir(fenster),
                      msg="Member spieler nicht gefunden.")
        self.assertTrue(issubclass(type(fenster.spieler), arcade.Sprite),
                        msg="Member spieler ist kein Sprite sondern {}".format(type(fenster.spieler)))

    def test_50_spieler_wird_gezeichnet(self):
        fenster = heute.FindeDenSchnellstenWeg(600, 600)
        fenster.spieler = MagicMock()
        self.assertFalse(fenster.spieler.draw.called,
                         msg="Bevor on_draw aufgerufen wird, sollte spierer.draw() auch nicht ausgeführt werden.")
        fenster.on_draw()
        self.assertTrue(fenster.spieler.draw.called,
                        msg="Wenn on_draw() aufgerufen wird, sollte spieler.draw() aber aufgerufen werden")

    def test_60_spieler_startposition(self):
        fenster = heute.FindeDenSchnellstenWeg(600, 600)
        self.assertEqual(fenster.spieler.position, (50, 50))