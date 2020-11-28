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

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Hier werden alle Objekte/Figuren/... des Spiels gezeichnet.
        Dazu wird für die einzelnen Objekte die `draw()`-Methode aufgerufen.
        """
        arcade.start_render()  # muss zuallererst aufgerufen werden
        self.spieler.draw()

    def on_update(self, delta_time):
        """
        Hier werden die Objekte/Figuren/... aktualisiert -- beispielsweise
        deren Position neu gesetzt.
        Für Sprites kann man die `update()`-Methode aufrufen, damit sie ihre
        Position basierend auf ihrer letzten Position und den Eigenschaften
        `change_x`, `change_y` und `change_angle` aktualisiert.
        """
        pass

    def on_key_press(self, key, modifiers):
        """
        Hier kann man darauf reagieren, dass eine Taste auf der Tastatur
        gedrückt wurde.
        `key` enthält dann einen Bezeichner für die Taste, bspw.
        `arcade.key.A` für die Taste A oder `arcade.key.LEFT` für die
        Pfeil-nach-links-Taste.
        """
        pass


def spiele_spiel():
    window = FindeDenSchnellstenWeg(1000, 800)
    arcade.run()

if __name__ == "__main__":
    spiele_spiel()