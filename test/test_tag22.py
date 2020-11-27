from unittest import TestCase
from unittest.mock import MagicMock

try:
    from pyventskalender import tag22_loesung as heute
except ImportError:
    from pyventskalender import tag22 as heute

try:
    import arcade
except ImportError:
    print("Fehler beim importieren von 'arcade'.  Bitte installiere arcade und aktiviere das venv in das du es installiert hast.")


class Tag22Tests(TestCase):

    def test_10_tasten_fuehren_zu_change(self):
        fenster = heute.FindeDenSchnellstenWeg(600, 600)
        self.assertEqual(fenster.spieler.change_x, 0, 
                         msg="Initial sollte der Spieler sich nicht bewegen.")
        self.assertEqual(fenster.spieler.change_y, 0,
                         msg="Initial sollte der Spieler sich nicht bewegen.")
        fenster.on_key_press(arcade.key.LEFT, 0)
        self.assertEqual(fenster.spieler.change_x, -5, msg="Links -> x=-5")
        self.assertEqual(fenster.spieler.change_y,  0, msg="Links -> y=0")
        fenster.on_key_press(arcade.key.RIGHT, 0)
        self.assertEqual(fenster.spieler.change_x,  5, msg="Rechts -> x=5")
        self.assertEqual(fenster.spieler.change_y,  0, msg="Rechts -> y=0")
        fenster.on_key_press(arcade.key.UP, 0)
        self.assertEqual(fenster.spieler.change_x,  0, msg="Hoch -> x=0")
        self.assertEqual(fenster.spieler.change_y,  5, msg="Hoch -> y=5")
        fenster.on_key_press(arcade.key.DOWN, 0)
        self.assertEqual(fenster.spieler.change_x,  0, msg="Runter -> x=0")
        self.assertEqual(fenster.spieler.change_y, -5, msg="Runter -> y=-5")

    def test_20_update_in_on_change(self):
        fenster = heute.FindeDenSchnellstenWeg(600, 600)
        fenster.spieler = MagicMock()
        self.assertFalse(fenster.spieler.update.called,
                         msg="Ohne on_update sollte spieler.update() nicht aufgerufen werden.")
        fenster.on_key_press(arcade.key.DOWN, 0)
        self.assertFalse(fenster.spieler.update.called,
                         msg="Wegen on_key_press sollte spieler.update() nicht aufgerufen werden.")
        fenster.on_update(0.2)
        self.assertEqual(fenster.spieler.update.call_count, 1,
                         msg="In on_update sollte spieler.update genau einmal aufgerufen werden.")

    def test_30_ziel(self):
        fenster = heute.FindeDenSchnellstenWeg(600, 600)
        self.assertIn("ziel", dir(fenster),
                      msg="Member ziel fehlt")
        self.assertTrue(issubclass(type(fenster.ziel), arcade.Sprite), msg="Ziel ist kein Sprite sondern {}".format(type(fenster.ziel)))

    def test_40_ziel_position(self):
        for breite, hoehe in [(400, 500), (500, 900), (1000, 1000)]:
            fenster = heute.FindeDenSchnellstenWeg(breite, hoehe)
            self.assertEqual(fenster.ziel.position, (0.9 * breite, 0.9 * hoehe))

    def test_50_draw_reihenfolge(self):
        fenster = heute.FindeDenSchnellstenWeg(500, 500)
        draw_aufrufe_reihenfolge = []
        fenster.spieler.draw = MagicMock()
        fenster.spieler.draw.side_effect = lambda : draw_aufrufe_reihenfolge.append("spieler")
        fenster.ziel.draw = MagicMock()
        fenster.ziel.draw.side_effect = lambda : draw_aufrufe_reihenfolge.append("ziel")
        fenster.on_draw()

        self.assertEqual(draw_aufrufe_reihenfolge, ["ziel", "spieler"],
                         msg="Die Reihenfolge der draw()-Aufrufe ist {} (was nicht so sein sollte)".format(draw_aufrufe_reihenfolge))