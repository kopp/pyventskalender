from unittest import TestCase
from unittest.mock import MagicMock, patch

try:
    from pyventskalender import tag23_loesung as heute
except ImportError:
    from pyventskalender import tag23 as heute

try:
    import arcade
except ImportError:
    print("Fehler beim importieren von 'arcade'.  Bitte installiere arcade und aktiviere das venv in das du es installiert hast.")


class Tag23Tests(TestCase):

    def test_10_geschafft(self):
        fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
        self.assertIn("geschafft", dir(fenster),
                 msg="Member geschafft fehlt.")
        self.assertFalse(fenster.geschafft,
                         msg="Initial sollte geschafft False sein.")
        fenster.on_update(0.1)
        fenster.on_update(0.1)
        fenster.on_update(0.1)
        self.assertFalse(fenster.geschafft,
                         msg="Auch nach ein paar Updates sollte geschafft False sein.")

        fenster.spieler.position = fenster.ziel.position
        fenster.on_update(0.1)
        self.assertTrue(fenster.geschafft,
                         msg="Wenn der spieler auf dem ziel steht, sollte geschafft True sein.")

    def test_20_text_geschafft(self):
        with patch("arcade.draw_text"):
            fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
            fenster.on_draw()
            self.assertFalse(fenster.geschafft)
            self.assertFalse(arcade.draw_text.called,
                             msg="draw_text sollte nicht aufgerufen werden, wenn man es nicht geschafft hat.")
            fenster.geschafft = True
            fenster.on_draw()
            self.assertTrue(arcade.draw_text.called,
                             msg="draw_text sollte aufgerufen werden, wenn man es geschafft hat.")
            self.assertIn("Geschafft", arcade.draw_text.call_args.args,
                          msg="draw_text sollte mit 'Geschafft' aufgerufen werden, nicht {}".format(arcade.draw_text.call_args.args))

    def test_30_stop_wenn_beendet(self):
        fenster = heute.FindeDenSchnellstenWeg(1000, 1000)
        fenster.spieler.stop = MagicMock()
        fenster.spieler.position = fenster.ziel.position
        fenster.on_update(0.1)
        self.assertTrue(fenster.spieler.stop.called,
                        msg="stop() für den spieler sollte aufgerufen werden, wenn er am Ziel ist.")
