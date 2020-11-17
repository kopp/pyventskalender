# Heute spielen wir "Eine Kleine Satzwerkstatt".
#
# Bei dem Spiel baut man Sätze aus vier Teilen, die jeweils
# zufällig gewählt sind:
#  - eine Adverbiale (bspw. Bei Vollmond)
#  - einem Verb in er/sie/es-Form (bspw. versteckt)
#  - einem Subjekt (bspw. mein Zahnarzt)
#  - einem Objekt (bspw. die Alpen)

# %%
# Hier ein paar Beispiele -- gerne erweitern!

MOEGLICHE_ADVERBIALE = [
    "Beim Programmieren",
    "Am PC",
    "Im ICE",
    "An der Kasse",
    "Beim Schaukeln",
    "Bei Vollmond",
    "Auf dem Weihnachtsmarkt",
]

MOEGLICHE_VERBEN = [
    "liebt",
    "kontrolliert",
    "sucht",
    "springt",
    "schenkt mir",
    "vergisst",
    "lobt",
]

MOEGLICHE_SUBJEKTE = [
    "meine Frau",
    "der Schaffner",
    "jeder",
    "der 7. Zwerg",
    "die Verkäuferin",
    "das Nachbarskind",
]

MOEGLICHE_OBJEKTE = [
    "Python",
    "frische Kräuter",
    "die roten Schuhe",
    "einen Kaugummi",
    "den neuen Hut",
    "einen Bademantel",
    "den Busfahrer",
]

# %%
# Wir haben also vier Satzglieder, die wir zu einem Satz zusamenfassen wollen.
# Für diese beiden Teile, Satz und Satzglied, erstellen wir Typen.
# Anfangs sind diese noch ganz leer, sie werden sich bald füllen.

class Satzglied:
    pass

class Satz:
    pass

# %%
# Sorge jetzt dafür, dass wenn ein Satz erzeugt wird, er die vier Member
# `adverbiale`, `verb`, `subjekt` und `objekt` anlegt.


# %%
# Wir wollen die Satzglieder zufällig aus einer Liste auswählen.
# Sorge nun dafür, dass man bei der Erstellung von `Satzglied` die Liste der
# möglichen Wörter übergeben kann und diese im Member `moeglichkeiten`
# gespeichert werden.
# Passe dann deinen Code in `Satz` so an, dass die richtigen Listen von oben
# korrekt übergeben werden.
# Der Member `text` von `Satzglied` soll initial das erste Element aus der
# Liste enthalten.


# %%
# Solltest du nicht weiter kommen, hier ein Tip:

import base64

def decodiere_wort(codiertes_wort: bytes) -> str:
    return base64.b64decode(codiertes_wort).decode("utf-8")

decodiere_wort(
b'VGlwOiBCZWltIEVyc3RlbGxlbiB3aXJkIF9faW5pdF9fIGF1ZmdlcnVmZW4uICBBbHMgZXJzdGVuIFBhcmFtZXRlciBoYXQgX19pbml0X18gaW1tZXIgc2VsZiwgZGllIHdlaXRlcmVuIFBhcmFtZXRlciBrYW5uIG1hbiBkYW5uIG5hY2ggZ3VzdG8gdmVyd2VuZGVuLg=='
)


# %%
# Damit könenn wir heute schon einen ersten Satz ausgeben -- wenn das auch noch
# kein schöner Code und auch keine schöne Ausgabe ist.

def ersten_satz_ausgeben():
    erster_satz = Satz()
    return erster_satz.adverbiale.text, erster_satz.verb.text, erster_satz.subjekt.text, erster_satz.objekt.text
# %%
