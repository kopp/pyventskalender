import re

EINZUSETZENDES_WORT_RE = re.compile(r"(<.*?>)")

def mad_libs(geschichte_mit_zu_ersetzenden_worten: str) -> str:
    geschichte = geschichte_mit_zu_ersetzenden_worten
    for wort in EINZUSETZENDES_WORT_RE.findall(geschichte_mit_zu_ersetzenden_worten):
        ersetzung = input(wort)
        geschichte = geschichte.replace(wort, ersetzung)
    return geschichte