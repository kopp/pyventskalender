from unittest import TestCase
from unittest.mock import MagicMock, patch

try:
    from pyventskalender import tag24_loesung as heute
    MODULE_NAME = "pyventskalender.tag24_loesung"
except ImportError:
    from pyventskalender import tag24 as heute
    MODULE_NAME = "pyventskalender.tag24"

import pyventskalender

try:
    import arcade
except ImportError:
    print("Fehler beim importieren von 'arcade'.  Bitte installiere arcade und aktiviere das venv in das du es installiert hast.")

import random


class Tag24Tests(TestCase):

    def test_10_hindernisse_sind_sprites(self):
        fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
        self.assertIn("hindernisse", dir(fenster),
                      msg="kein Member hindernisse")
        self.assertEqual(len(fenster.hindernisse), 15,
                         msg="Ich hätte eine Liste mit 15 Hindernissen erwartet")
        self.assertTrue(
            all([issubclass(type(hindernis), arcade.Sprite) for hindernis in fenster.hindernisse]),
            msg="Die Hindernisse sollten Sprites sein."
        )

    def test_20_hindernisse_positionen(self):
        if "randint" in dir(heute):
            to_patch = MODULE_NAME + ".randint"
        else:
            to_patch = "random.randint"
        with patch(to_patch):
            if to_patch.startswith("pyventskalender.tag24_loesung"):
                mock = pyventskalender.tag24_loesung.randint
            elif to_patch.startswith("pyventskalender.tag24"):
                mock = pyventskalender.tag24.randint
            else:
                mock = random.randint
            self.assertFalse(mock.called,
                             msg="hier geht etwas im Test schief :(")
            fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
            self.assertEqual(mock.call_count, 30,
                             msg="Erwartet wären 30 Aufrufe von randint -- 2 pro Hindernis; es sind aber {}".format(mock.call_count))
            for aufruf in mock.call_args_list:
                self.assertGreaterEqual(aufruf.args[0], 100,
                                        msg="Erwartet war ein Mindestwert von 100 für x-Wert des Hindernisses")
                self.assertGreaterEqual(aufruf.args[1], 100,
                                        msg="Erwartet war ein Mindestwert von 100 für y-Wert des Hindernisses")

    def test_30_hindernisse_gezeichnet(self):
        fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
        for hindernis in fenster.hindernisse:
            hindernis.draw = MagicMock()
        fenster.on_draw()
        self.assertTrue(
            all([hindernis.draw.called for hindernis in fenster.hindernisse]),
            msg="Bei on_draw solte draw() für alle Hindernisse ausgeführt werden."
        )

    def test_40_verloren(self):
        with patch("arcade.draw_text"):
            fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
            fenster.spieler.stop = MagicMock()
            self.assertIn("verloren", dir(fenster),
                    msg="Member verloren fehlt.")
            self.assertFalse(fenster.verloren,
                            msg="Initial sollte verloren False sein.")
            self.assertFalse(fenster.spieler.stop.called,
                            msg="Der Spieler soll anfangs nicht gestoppt worden sein.")
            fenster.on_update(0.1)
            fenster.on_update(0.1)
            fenster.on_update(0.1)
            self.assertFalse(fenster.verloren,
                            msg="Auch nach ein paar Updates sollte verloren False sein.")

            hindernis_no = random.randint(0, 14)
            fenster.spieler.position = fenster.hindernisse[hindernis_no].position
            fenster.on_update(0.1)
            self.assertTrue(fenster.verloren,
                            msg="Wenn der spieler auf Hindernis {} steht, sollte verloren True sein.".format(hindernis_no))
            self.assertTrue(fenster.spieler.stop.called,
                            msg="Der Spieler soll gestoppt werden, wenn er verloren hat.")
            fenster.on_draw()
            self.assertTrue(arcade.draw_text.called,
                            msg="Wenn man verloren hat, sollte on_draw aufgerufen werden.")
            self.assertIn("Verloren :(", arcade.draw_text.call_args.args,
                          msg="draw_text sollte mit 'Verloren :(' aufgerufen werden, nicht {}".format(arcade.draw_text.call_args.args))

    def test_50_hindernisse_entfernen_integriert(self):
        fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
        self.assertIn("nahe_hindernisse_entfernen", dir(fenster),
                      msg="Methode nahe_hindernisse_entfernen ist nicht in FindeDenSchnellstenWeg.")
        fenster.nahe_hindernisse_entfernen = MagicMock()
        fenster.on_key_press(arcade.key.SPACE, 0)
        self.assertTrue(fenster.nahe_hindernisse_entfernen.called,
                        msg="nahe_hindernisse_entfernen sollte aufgerufen werden, wenn die Leertaste gerdrückt wird.")
