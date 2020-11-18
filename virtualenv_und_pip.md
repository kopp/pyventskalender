# Übersicht

1. Virtual Environment anlegen:

        python -m venv --system-site-packages venv

1. Virtual Environemt aktivieren:
    - Strg+Shift+P drücken
    - "Python: Select Interpreter"
    - "Enter Interpreter Path"
    - ".\venv\Scripts\python.exe"

1. Installieren mit `pip` von [pypi.org](https://pypi.org/)

        pip install <paketname>

# Virtualenv

## Idee

Damit man Pakete später wieder einfach löschen kann, legt man am besten ein Virtual Environment an.

## Anlegen

Das geht am besten in der Konsole `powershell`.
In Visual Studio Code kannst du eine aufmachen, indem du oben auf Terminal und dann New Terminal (oder Neues Terminal) gehst.
Gib hier ein:

    python -m venv --system-site-packages venv

Es müsste dann der Ordner `venv` angelegt werden.

## Aktivieren

Wenn du Glück hast, fragt dich Visual Studio Code direkt, ob du das Virtual Environent aktivieren willst -- sag "Ja".

Wenn nicht, dann kannst du jetzt das Virtual Environment aktivieren.
Am einfachsten geht das, wenn du die Konsole schließt (`exit`) und dann Strg+Shift+P drückst, dann geht oben eine Eingabe auf.
Gibt dort "Python: Select Interpreter" ein und wähle das Element aus (Enter).
Wähle dort "Enter Interpreter Path" und gib ".\venv\Scripts\python.exe" ein (Linux/Mac: "./venv/bin/python").
Wenn du jetzt eine neue Konsole aufmachst, dann sorgt Visual Studio Code dafür, dass du das Virtual Environment nutzt.

## Prüfen, ob das virtual environment aktiviert ist

Um zu prüfen, ob sie das Virtual Environment verwendet, gib
    Get-Command python
ein (Linux/Mac User: `which python`).
Das sollte den aktuellen Ordner mit "venv\Scripts\python" ausgeben (Linux/Mac: "venv/bin/python").
Wenn dem nicht so ist, Konsole schließen (`exit`) und neu öffnen und hoffen.
Wenn dem immer noch nicht so ist, das Virtual Environment nochmal aktivieren.


# pip

Um etwas zu installieren öffne eine Konsole und gib ein

    pip install <name des pakets>

Unter
[pypi.org](https://pypi.org/)
findest du eine große List von öffentlich verfügbaren Paketen.