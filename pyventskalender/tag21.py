# Heute beginnen wir mit eineme eigenen einfachen Spiel.

# %%
# Die Library 'arcade' (siehe https://arcade.academy/) hilft, einfache Spiele
# in Python zu entwerfen.
# Installiere sie in dem Virtual Environment `venv`, das wir gestern schon
# angelegt haben.
# Hinweis: Wenn du unter Linux arbeitest, dann führe vorher aus:
#    pip install --compile --install-option=-O1 PilloW
# Wenn PilloW schon installiert ist, dann mache vorher
#    pip uninstall PilloW

# %%
# Will man ein Spiel prorammieren, empfiehlt es sich, in den vorhandenen
# Beispielen nach etwas zu suchen, das schon in die Richtung geht von dem, was
# man selber erreichen will.
# Hier ist eine Liste von einfachen Beispielen:
# https://arcade.academy/get_started.html
# Google hilft, mehr zu finden.
#
# Unser Spiel basieren wir auf der folgenden einfachen Klasse.
# Lasse die Zelle laufen und führe `spiel_spielen()` aus, um zu sehen, wie weit
# das Spiel schon ist.
#
# Hinweis: Die Funktionen, die mit on_ anfangen werden von der arcade-Library
# aufgerufen, wenn etwas bestimmtes passiert -- wenn eine Taste auf der
# Tastatur gerdückt wird (`on_key_press`) oder wenn es Zeit wird, die Figuren
# zu bewegen (`on_update`) oder alles zu zeichnen (`on_draw`).
# Die Library gibt vor, dass es diese Methoden gibt, der Spieleentwickler nutzt
# sie, indem er sinnvollen Code in sie reinschreibt.

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

## %%
# Füge jetzt einen Spieler ein.
# Dazu erstellst du in `__init__` ein Member `spieler`, das ein
# `arcade.Sprite`-Objekt sein soll.
# Dem gibst du als Argument das Bild mit, das dein Spieler haben soll.
# Hier sind mögliche Bilder:
# https://arcade.academy/resources.html
# (Hinweis: Um das Bild anzugeben verwendet man dann einen kompletten "Pfad",
# der mit :resources: beginn, also bspw. ":resources:images/enemies/frog.png")

# %%
# Startet man das Spiel, dann sieht man ihn bisher noch nicht.
# Dazu musst du ihn in `on_draw` aufnehmen -- siehe die Beschreibung dort.
# Jetzt müsstest du im linken unteren Eck deine Figur ein klein wenig sehen.

# %%
# Die Positionen in dem Fenster werden mit zwei Zahlen angegeben.
# Die Höhe und Breite davon geben wir im Konstruktor an (also 1000 breit und
# 800 hoch), die linke untere Ecke hat die Koordinaten 0, 0 -- dort startet
# deine Figur.
# Setze sie bitte an die Position 50, 50, damit man sie besser sehen kann.
# (Hinweis: die Position steht im Member `position`

# %%
# Hinweis: Mit `if __name__ == "__main__"`` prüft man ab, ob die Datei gerade
# als Script ausgeführt wird -- also per `python tag21.py` in der Kommandozeile
# oder per Doppelklick im Dateiexplorer oder per Klick auf den kleinen grünen
# Pfeil rechts oben in Visual Studio Code.
# Wenn dem so ist, wird das Spiel direkt gestartet.
# Für das Spiel ist es besser, das komplette Spiel in als Script zu laden, als
# es als "Run Cell" auszuführen, weil sonst von "alten" Ausführungen des Spiels
# noch "Reste" übrig bleiben können, die das Spiel "kaputtmachen".