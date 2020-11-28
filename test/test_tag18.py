from unittest import TestCase

try:
    from pyventskalender import tag18_loesung as heute
except ImportError:
    from pyventskalender import tag18 as heute


class Tag18Tests(TestCase):

    def test_10_elemente_in_satz(self):
        frischer_satz = heute.Satz()
        for satzteil in ["adverbiale", "verb", "subjekt", "objekt"]:
            self.assertIn(satzteil, dir(frischer_satz),
                          msg=f"Satz hat noch keinen Member {satzteil}")
        self.assertEqual(type(frischer_satz.adverbiale), heute.Satzglied,
                         msg="Die adverbiale sollte ein Satzglied sein, kein {}".format(
                             type(frischer_satz.adverbiale)))
        self.assertEqual(type(frischer_satz.verb), heute.Satzglied)
        self.assertEqual(type(frischer_satz.subjekt), heute.Satzglied)
        self.assertEqual(type(frischer_satz.objekt), heute.Satzglied)

    def test_20_moeglichkeiten_in_satzglied(self):
        moeglichkeiten = ["a", "b"]
        satzglied = heute.Satzglied(moeglichkeiten)
        self.assertEqual(satzglied.moeglichkeiten, moeglichkeiten)
        self.assertEqual(satzglied.text, moeglichkeiten[0])

    def test_30_listen_in_satz_uebergeben(self):
        satz = heute.Satz()
        self.assertEqual(satz.adverbiale.moeglichkeiten, heute.MOEGLICHE_ADVERBIALE)
        self.assertEqual(satz.verb.moeglichkeiten, heute.MOEGLICHE_VERBEN)
        self.assertEqual(satz.subjekt.moeglichkeiten, heute.MOEGLICHE_SUBJEKTE)
        self.assertEqual(satz.objekt.moeglichkeiten, heute.MOEGLICHE_OBJEKTE)
