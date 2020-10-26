#%%
def ich_haette_gerne_so_viele_katzen(anzahl: int) -> str:
    text = "Ich hätte gerne {} Katze".format(anzahl)
    if anzahl > 1:
        text += "n"
    return text

# %%
# Damit können wir schon ein kleines Spiel bauen.
# Hier wird eine Zufallszahl zwischen 1 und 20 gewählt:
import random
zufallszahl = random.randint(1, 20)

# Die folgende Funktion soll ausgeben
# - "richtig, gefunden!" wenn man die korrekte Zahl angibt
# - "falsch, zu hoch", wenn die gesuchte Zahl niedriger ist oder
# - "falsch, zu niedrig", wenn die gesuchte Zahl höher ist
# Damit kann man dann immer wieder mit bspw. `ich_tippe_auf(5)` einen Tip
# abgeben, und die Funktion sagt, wie man weiter raten muss.
# Ein solches Spiel könnte dann so ablaufen:
#    ich_tippe_auf(5) -> 'falsch, zu niedrig'
#    ich_tippe_auf(10) -> 'falsch, zu hoch'
#    ich_tippe_auf(7) -> 'richtig, gefunden!'

def ich_tippe_auf(zahl: int):
    if zahl > zufallszahl:
        return "falsch, zu hoch"
    elif zahl < zufallszahl:
        return "falsch, zu niedrig"
    else:
        return "richtig, gefunden!"
