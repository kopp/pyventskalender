import arcade
from random import randint, random

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
        self.verloren = False
        self.zurueckgelegter_weg = 0

        self.hindernisse = []
        for _ in range(15):
            hindernis = arcade.Sprite(":resources:images/tiles/boxCrate_double.png")
            hindernis.position = randint(100, self.breite), randint(100, self.hoehe)
            self.hindernisse.append(hindernis)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Hier werden alle Objekte/Figuren/... des Spiels gezeichnet.
        Dazu wird für die einzelnen Objekte die `draw()`-Methode aufgerufen.
        """
        arcade.start_render()  # muss zuallererst aufgerufen werden
        for hindernis in self.hindernisse:
            hindernis.draw()
        self.ziel.draw()
        self.spieler.draw()
        if self.geschafft:
            arcade.draw_text("Geschafft", self.breite // 3, self.hoehe // 2, arcade.color.RED, 50)
            arcade.draw_text("Zurückgelegter Weg: {}".format(self.zurueckgelegter_weg),
                             self.breite // 3, self.hoehe // 3, arcade.color.BLACK, 30)
        if self.verloren:
            arcade.draw_text("Verloren :(", self.breite // 3, self.hoehe // 2, arcade.color.RED, 50)

    def _weg_aufaddieren(self, position_alt, position_neu):
        # Verwende Manhattan-Distanz -- der Spieler kann nur nach
        # rechts/links/oben/unten, nicht schräg.
        delta_x = abs(position_alt[0] - position_neu[0])
        delta_y = abs(position_alt[1] - position_neu[1])
        self.zurueckgelegter_weg += delta_x + delta_y

    def on_update(self, delta_time):
        """
        Hier werden die Objekte/Figuren/... aktualisiert -- beispielsweise
        deren Position neu gesetzt.
        Für Sprites kann man die `update()`-Methode aufrufen, damit sie ihre
        Position basierend auf ihrer letzten Position und den Eigenschaften
        `change_x`, `change_y` und `change_angle` aktualisiert.
        """
        position_alt = self.spieler.position
        self.spieler.update()
        position_neu = self.spieler.position
        self._weg_aufaddieren(position_alt, position_neu)

        self.geschafft = arcade.check_for_collision(self.spieler, self.ziel)

        for hindernis in self.hindernisse:
            if arcade.check_for_collision(self.spieler, hindernis):
                self.verloren = True
            hindernis.update()

        if self.geschafft or self.verloren:
            self.spieler.stop()
            for hindernis in self.hindernisse:
                hindernis.stop()

    def nahe_hindernisse_entfernen(self):
        for hindernis in self.hindernisse:
            abstand = arcade.get_distance_between_sprites(self.spieler, hindernis)
            if abstand < 240:
                self.hindernisse.remove(hindernis)
            else:
                hindernis.change_angle += 0.1 * random()
                hindernis.change_x += 2 * random()
                hindernis.change_y += 2 * random()

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
        elif key == arcade.key.RIGHT:
            self.spieler.change_x = 5
            self.spieler.change_y = 0
        elif key == arcade.key.UP:
            self.spieler.change_x = 0
            self.spieler.change_y = 5
        elif key == arcade.key.DOWN:
            self.spieler.change_x = 0
            self.spieler.change_y = -5
        elif key == arcade.key.SPACE:
            self.nahe_hindernisse_entfernen()


def spiele_spiel():
    window = FindeDenSchnellstenWeg(1000, 800)
    arcade.run()

if __name__ == "__main__":
    spiele_spiel()

# %%
# Jetzt wollen wir es dem Spieler noch ein klein wenig schwerer machen, sein
# Ziel zu erreichen.
# Dafür platzieren wir eine Menge von Hindernissen.
# Jedes Hindernis ist selbst wieder ein `arcade.Sprite` -- such dir wieder eine
# passende Resource aus.
# Erstelle eine Liste `hindernisse` als Member, die 15 Hindernisse an
# zufälligen Stellen enthält.
# Hinweis: Damit `spieler` nicht direkt am Anfang mit einem Hindernis
# kollidiert, wähle für die x- und y-Komponente jeweils mindestens 100.
# Um eine Zufallszahl zwischen a und b zu bekommen, verwende `random.randint(a, b)`.
# Hinweis: Der `spieler` kann auch außerhalb des sichtbaren Spielfelds laufen.

# %%
# Wenn der `spieler` ein Hindernis aus `hindernisse` berührt, hat er verloren.
# Prüfe also, ob er eines berührt und wenn ja setze `verloren` auf True
# (initial soll das auf False sein), halte den Spieler an und schreibe in
# `on_draw` den Text "Verloren :(" aus.

# %%
# Und weil heute Weihnachten ist, hier noch ein kleines Geschenk:
# Füge die folgende Methode in die Klasse ein und rufe sie auf, wenn die
# Leertaste gedrückt wird.
# Damit kannst du dir den Weg "Freiräumen"
# Viel Spaß :)

def nahe_hindernisse_entfernen(self):
    for hindernis in self.hindernisse:
        abstand = arcade.get_distance_between_sprites(self.spieler, hindernis)
        if abstand < 240:
            self.hindernisse.remove(hindernis)
