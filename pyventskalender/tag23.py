# Weiter geht es mit dem Spiel...

# %%
# Gestern hatten wir ungefähr so aufgehört:

import arcade

class FindeDenSchnellstenWeg(arcade.Window):
    """
    In dieser Klasse implementieren wir das Spiel.
    """

    def __init__(self, breite, hoehe):
        super().__init__(breite, hoehe, "Finde den schnellsten Weg")
        self.breite = breite
        self.hoehe = hoehe

        self.spieler = arcade.Sprite(":resources:images/enemies/frog.png")
        self.spieler.position = 50, 50

        self.ziel = arcade.Sprite(":resources:images/enemies/slimeGreen.png")
        self.ziel.position = 0.9 * self.breite, 0.9 * self.hoehe

        self.geschafft = False

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Hier werden alle Objekte/Figuren/... des Spiels gezeichnet.
        Dazu wird für die einzelnen Objekte die `draw()`-Methode aufgerufen.
        """
        arcade.start_render()  # muss zuallererst aufgerufen werden
        self.ziel.draw()
        self.spieler.draw()
        if self.geschafft:
            arcade.draw_text("Geschafft", 0.3 * self.breite, 0.4 * self.hoehe, arcade.color.RED, 50)

    def on_update(self, delta_time):
        """
        Hier werden die Objekte/Figuren/... aktualisiert -- beispielsweise
        deren Position neu gesetzt.
        Für Sprites kann man die `update()`-Methode aufrufen, damit sie ihre
        Position basierend auf ihrer letzten Position und den Eigenschaften
        `change_x`, `change_y` und `change_angle` aktualisiert.
        """
        self.spieler.update()
        self.geschafft = arcade.check_for_collision(self.spieler, self.ziel)
        if self.geschafft:
            self.spieler.stop()

    def on_key_press(self, key, modifiers):
        """
        Hier kann man darauf reagieren, dass eine Taste auf der Tastatur
        gedrückt wurde.
        `key` enthält dann einen Bezeichner für die Taste, bspw.
        `arcade.key.A` für die Taste A oder `arcade.key.LEFT` für die
        Pfeil-nach-links-Taste.
        """
        if key == arcade.key.LEFT:
            self.spieler.change_x = -5
            self.spieler.change_y = 0
        if key == arcade.key.RIGHT:
            self.spieler.change_x = 5
            self.spieler.change_y = 0
        if key == arcade.key.UP:
            self.spieler.change_x = 0
            self.spieler.change_y = 5
        if key == arcade.key.DOWN:
            self.spieler.change_x = 0
            self.spieler.change_y = -5


def spiele_spiel():
    window = FindeDenSchnellstenWeg(1000, 800)
    arcade.run()

if __name__ == "__main__":
    spiele_spiel()



# %%
# Wenn wir ins Ziel kommen, wollen wir das auch merken.
# Dazu wollen wir wissen, wann unser `spieler` das `ziel` berührt.
# Dazu gibt es die Funktion `arcade.check_for_collision`.
# Schreibe die Funktion aus und halte die Maus daüber, dann müsste dir eine
# Hilfe angezeigt werden, mit der du arbeiten kannst.
# Du solltest den Member `geschafft` initial auf False setzen und auf True wenn
# das Ziel erreicht ist.
# Das prüfst du am besten in `on_update` -- hier bewegt sich der `spieler`.

# %%
# Wenn der Spieler es geschafft hat, dann soll er das auch sehen.
# Schreibe deshalb in der `on_draw`-Methode den Text "Geschafft", sobald der
# `spieler` das `ziel` erreicht hat.
# Dabei hilft dir `arcade.draw_text`.

# %%
# Dir ist sicher schon aufgefallen, dass der `spieler` noch weiter läuft, auch
# wenn das Spiel schon beendet ist.
# Verwende seine `stop`-Methode, wenn er das Ziel erreicht hat, damit er sich
# nicht weiter bewegt.