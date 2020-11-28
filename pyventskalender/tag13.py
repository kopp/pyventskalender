# Heute wollen wir uns anschauen, wie man das Spiel
# [Mad Libs](https://de.wikipedia.org/wiki/Mad_Libs) in Python umsetzen kann.


# %%
# Wir wollen unseren Satz mit Satzbausteinen beschreiben.
# Dazu verwenden wir `< >`-Klammern im Text, um die zu ersetzenden Teile zu
# markieren, das sieht dann bspw. so aus:
geschichte = "Eines Tages <Verb in Vergangenheitsform> <Name> nach New York um <Substantiv> zu sehen."

# %% Regexp erzeugen -- Test 10
# Erstelle jetzt eine Regular Expression, die ein einzelnes dieser zu
# ersetzenden Teile findet (also eine Gruppe enthält, die den Teil in <>
# findet).
# In `"foo <bar> asdf"` sollte also bspw. `<bar>` gefunden werden.
# In `"foo <bar> asdf <x>"` sollte `<bar>` und `<x>` gefunden werden.
#
# Hinweis: Benutze die interaktive Konsole, um die Regular Expression zu
# testen. Fange mit einfachen Texten wie `"<x>"` an, und steigere dich langsam.
# Um in einem Text `text` alle Vorkommnisse des regulären Ausdrucks `reg` zu
# finden, verwende `reg.findall(text)`.
# Hinweis: Solltest du in einem Text mehrere `<>`-Blöcke auf einmal finden
# (also in `"a <b> c <d> e"` den Block `<b> c <d>`), dann kannst du ein `?` in
# der Regular Expression verwenden, damit deine Gruppe so kurz wie möglich wird
# und damit hoffentlich nur noch `<b>` findet.

EINZUSETZENDES_WORT_RE = "ERSETZE MICH"


# %%
# Solltest du nicht weiterkommen, hier ein Tip:

import base64
base64.b64decode(
    b'RGVpbmUgUmVndWxhciBFeHByZXNzaW9uIHNvbGx0ZSBlaW5lIEdydXBwZSBgKClgIGVudGhhbHRlbiwgaW4gZGVyIGV0d2FzIGRyaW4gc3RlaHQu'
).decode("utf-8")

# %%
# Hier noch ein Tip

import base64
base64.b64decode(
    b'RGllIEtsYW1tZXJuIGA8YCB1bmQgYD5gIHNvbGx0ZW4gaW4gZGVyIEdydXBwZSBzZWluLg=='
).decode("utf-8")


# %%
# Hier der letzte Tip

import base64
base64.b64decode(
    b'RGVyIEF1c2RydWNrIGAoPC4qPz4pYCBmaW5kZXQgVGV4dCwgZGVyIG1pdCBgPGAgYW5mw6RuZ3QsIGRhbm4gVGV4dCBlbnRow6RsdCB1bmQgZGFubiBtaXQgYD5gIGVuZGV0Lg=='
).decode("utf-8")


# %% Mad Libs -- Test 20
# Jetzt zum eigentlichen Spiel:
# Vervollständige die Funktion, sodass sie
#  - zuerst alle zu ersetzenden Worte in der Geschichte findet
#  - für jedes dieser Worte den Nutzer nach einer Eingabe fragt
#  - in dem Text das Wort mit der Eingabe ersetzt (hatten wir noch nicht --
#    vielleicht kann Google helfen?)
#  - am Ende die Geschichte mit allen ersetzten Wörtern zurückgibt

def mad_libs(geschichte_mit_zu_ersetzenden_worten: str) -> str:
    pass

# %%
# Überleg dir noch ein paar Geschichten und spiele das Spiel auch mit anderen.

geschichten = [
    "Eines Tages <Verb in Vergangenheitsform> <Name> nach New York um <Substantiv> zu sehen.",
]

geschichten_codiert = [
    b'SWNoIDxCZXdlZ3VuZ3N3ZXJiIGluIGljaC1Gb3JtIHVuZCBWZXJnYW5nZW5oZWl0PiBpbiA8U3RhZHQ+IHp1IGRlbiBLbMOkbmdlbiBlaW5lcyA8TXVzaWtpbnN0cnVtZW50cz4u',
    b'RGVyIE5vYmVscHJlaXMgZsO8ciA8V2lzc2Vuc2NoYWZ0PiBnZWh0IGRpZXNlcyBKYWhyIGFuIDxQZXJzb24+IGbDvHIgQmVpdHLDpGdlIHp1IDxUZWNobm9sb2dpZT4u',
]

import base64

def spiele_mit_geschichten():
    for geschichte in geschichten:
        print(mad_libs(geschichte))
    for geschichte_codiert in geschichten_codiert:
        geschichte = base64.b64decode(geschichte_codiert).decode("utf-8")
        print(mad_libs(geschichte))
