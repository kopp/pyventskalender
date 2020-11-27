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

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Hier werden alle Objekte/Figuren/... des Spiels gezeichnet.
        Dazu wird für die einzelnen Objekte die `draw()`-Methode aufgerufen.
        """
        arcade.start_render()  # muss zuallererst aufgerufen werden
        self.ziel.draw()
        self.spieler.draw()

    def on_update(self, delta_time):
        """
        Hier werden die Objekte/Figuren/... aktualisiert -- beispielsweise
        deren Position neu gesetzt.
        Für Sprites kann man die `update()`-Methode aufrufen, damit sie ihre
        Position basierend auf ihrer letzten Position und den Eigenschaften
        `change_x`, `change_y` und `change_angle` aktualisiert.
        """
        self.spieler.update()

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

# %% Spieler bewegen -- Tests 10 20
# Jetzt wollen wir die Figur laufen lassen, indem wir die Pfeile auf der
# Tastatur drücken.
# Sorge dafür, dass wenn man den Pfeil nach rechts/links/oben/unten drückt,
# unser Spieler `change_x` und `change_y` entsprechend gesetzt bekommt:
# Drückt man nach links, soll er sich nur um 5 nach links bewegen und nicht
# nach oben/unten.
# Hinweis: Vergiss nicht, den Spieler in `on_update` aufzunehmen!


# %% Ziel -- Tests 30 40
# Schließlich wollen wir noch ein Ziel setzen, zu dem unser Spieler laufen
# soll.
# Erstelle dafür ein weiteres Sprite, `ziel`, das du nach rechts oben setzt --
# seine Position soll 90% der Breite und 90% der Höhe des Fensters sein.

# %% Übereinander zeichnen -- test 50
# Schaffst du es, mit der Figur bis zum Ziel zu laufen?
# Wenn du hinter dem Ziel "verschwindest", schaffst du es, dass du stattdessen
# über dem Ziel bist?