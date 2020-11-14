import base64
from random import choice

try:
    from pyventskalender.tag14_loesung import zu_ratendes_wort, galgenmannbild
    from pyventskalender.tag15_loesung import ist_aufgeben, ist_buchstabe, bewerte_geratenen_buchstaben
except ImportError:
    from tag14_loesung import zu_ratendes_wort, galgenmannbild
    from tag15_loesung import ist_aufgeben, ist_buchstabe, bewerte_geratenen_buchstaben


def galgenmannspiel(gesuchtes_wort: str):
    gesuchtes_wort = gesuchtes_wort.strip()
    noch_gesuchte_buchstaben = set(gesuchtes_wort.lower())
    falsch_geratene_buchstaben = []
    while True:
        print("Gesucht: ", zu_ratendes_wort(gesuchtes_wort, noch_gesuchte_buchstaben))
        eingabe = input("Rate einen Buchstaben")
        if ist_aufgeben(eingabe):
            print("Ok. Das Wort wäre gewesen: {}".format(gesuchtes_wort))
            return False
        if not ist_buchstabe(eingabe):
            print("Bitte genau einen Buchstaben angeben")
            continue
        buchstabe = eingabe.strip().lower()
        bewertung = bewerte_geratenen_buchstaben(buchstabe, noch_gesuchte_buchstaben, falsch_geratene_buchstaben)
        if bewertung == "richtig-geraten":
            print("Gut geraten!")
        elif bewertung == "falsch-geraten":
            print("{} ist leider falsch; bisher falsch geraten: {}".format(
                buchstabe,
                falsch_geratene_buchstaben))
            print(galgenmannbild(len(falsch_geratene_buchstaben)))
        elif bewertung == "gewonnen":
            print("Erraten!  Das Wort war {}".format(gesuchtes_wort))
            return True
        elif bewertung == "verloren":
            print("Leider nicht geklappt -- das Wort war {}".format(gesuchtes_wort))
            print(galgenmannbild(len(falsch_geratene_buchstaben)))
            return False




def codiere_wort(wort: str) -> bytes:
    return base64.b64encode(wort.encode("utf-8"))

def decodiere_wort(codiertes_wort: bytes) -> str:
    return base64.b64decode(codiertes_wort).decode("utf-8")


CODIERTE_WORTE = [
    b'QmV0dGh1cGZlcmw=',
    b'QmltYmFt',
    b'Qmx1YmJlcndhc3Nlcg==',
    b'RmxpdHpwaWVwZQ==',
    b'RnJhY2tzYXVzZW4=',
    b'SG9rdXNwb2t1cw==',
    b'SMO8ZnRnb2xk',
    b'S2FmZmVla2xhdHNjaA==',
    b'a2F0emVuasOkbW1lcmxpY2g=',
    b'S2F0emVua29wZnBmbGFzdGVy',
    b'S2xhdHNjaG1hdWw=',
    b'S2F1bHF1YXBwZQ==',
    b'S3LDpGh3aW5rZWxlaQ==',
    b'THVmdGlrdXM=',
    b'THVsYXRzY2g=',
    b'TWllc2VwZXRyaWdrZWl0',
    b'bXVja3Ntw6R1c2NoZW5zdGlsbA==',
    b'TmFzZW5mYWhycmFk',
    b'UHVyemVsYmF1bQ==',
    b'UHVzdGVrdWNoZW4=',
    b'UXVhZHJhdGxhdHNjaGVu',
    b'UXVhdHNjaGtvcGY=',
    b'cXVpZXRzY2hmaWRlbA==',
    b'UmFwcGVsa29wZg==',
    b'UmF0emVmdW1tZWw=',
    b'UnVtcGVsc3RpbHpjaGVu',
    b'U2NobWFja2Vz',
    b'U2NobW9sbHdpbmtlbA==',
    b'c2NobGFtcGFtcGVu',
    b'c2NobmFidWxpZXJlbg==',
    b'U2NobmFwc2lkZWU=',
    b'c2NobnVyenBpZXBlZ2Fs',
    b'U2Nod2l0emthc3Rlbg==',
    b'c3BsaXR0ZXJmYXNlcm5hY2t0',
    b'c3Rlcm5oYWdlbHZvbGw=',
    b'VG9sbHBhdHNjaCw=',
    b'VHJhbnTDvHRl',
    b'w7xiZXJwdXJ6ZWxu',
    b'dmVywq1rYcKtc2XCrW1hwq10dcKtY2tlbG4=',
    b'dmVyc2NobGltbWJlc3Nlcm4=',
    b'dmVyc2F1YmV1dGVsbg==',
    b'V2Fja2VsZGFja2Vs',
    b'V2FzY2hicmV0dGJhdWNo',
    b'V2F0c2NoZWxlbnRl',
    b'V2ltbWVsYmlsZA==',
    b'V29sa2Vua3Vja3Vja3NoZWlt',
    b'V29ubmVwcm9wcGVu',
    b'V3VjaHRicnVtbWU=',
]


def spiele_galgenmann():
    codiertes_wort = choice(CODIERTE_WORTE)
    wort = decodiere_wort(codiertes_wort)
    galgenmannspiel(wort)