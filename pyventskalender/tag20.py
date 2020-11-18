# Heute wollen wir ein externes Paket installieren.
#
# Dazu wird in Python `pip` verwendet.
#
# Setzt Datei virtualenv_und_pip.md voraus.

# %%
# Damit man Pakete später wieder einfach löschen kann, legt man am besten ein
# Virtual Environment an.
# Das geht am besten in der Konsole powershell.
# In Visual Studio Code kannst du eine aufmachen, indem du oben auf Terminal
# und dann New Terminal (oder Neues Terminal) gehst.
# Stelle bitte sicher, dass du in dem richtigen Ordner bist.
# Dazu kannst du `ls`, und es sollte dir u.a.
# `ich_will_meine_belohnung.py` anzeigen.
# Um jetzt das Virtual Environment anzulegen, gib ein:
#     python -m venv --system-site-packages venv
# Es müsste dann der Ordner `venv` angelegt werden.
# Wenn du Glück hast, fragt dich Visual Studio Code direkt, ob du das Virtual
# Environent aktivieren willst -- sag "Ja".
# Wenn nicht, dann kannst du jetzt das Virtual Environment aktivieren.
# Am einfachsten geht das, wenn du die Konsole schließt (`exit`) und dann
# Strg+Shift+P drückst, dann geht oben eine Eingabe auf.
# Gibt dort "Python: Select Interpreter" ein und wähle das Element aus (Enter).
# Wähle dort "Enter Interpreter Path" und gib ".\venv\Scripts\python.exe" ein
# (Linux/Mac: "./venv/bin/python").
# Wenn du jetzt eine neue Konsole aufmachst, dann sorgt Visual Studio Code
# dafür, dass du das Virtual Environment nutzt.

# %%
# Um jetzt tatsächlich dort etwas zu installieren öffne eine Konsole.
# Um zu prüfen, ob sie das Virtual Environment verwendet, gib
#     Get-Command python
# ein (Linux/Mac User: `which python`).
# Das sollte den aktuellen Ordner mit venv\Scripts\python ausgeben (Linux/Mac: "venv/bin/python").
# Wenn dem nicht so ist, Konsole schließen (`exit`) und neu öffnen und hoffen.
# Wenn dem immer noch nicht so ist, das Virtual Environment nochmal aktivieren.
# Jetzt kommt endlich die Installation:
#     pip install cat_fact

# %%
# War sie erfolgreich, kannst du
#     catFact
# eingeben und bekommst einen wichtigen Fakt über Katzen.


# %%
# Das können wir jetzt auch gleich in Code machen:

try:
    import requests
    from cat_fact.client import CatClient
    cat_client = CatClient(requests.Session(), "http://cat-fact.herokuapp.com")
    cat_client.get_random_fact("cat")
except ImportError:
    # Wir können offenbar nicht importieren, was wir wollen
    "Katzen sind tolle Tiere"
except ModuleNotFoundError:
    # Wir können offenbar nicht importieren, was wir wollen
    "Katzen sind tolle Tiere"

# %%
# Das ist ein ganz schön langer output, aber der Teil in "text" ist der interessante.
# Speichere doch den Output von `get_random_fact` (ein `dict`) und gib dir den
# Wert zum Schlüssel "text" aus.


# %%
# Die Wichtigsten Schritte zu Virtualenv findest du in `virtualenv_und_pip.md`.