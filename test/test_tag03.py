from unittest import TestCase
try:
    from pyventskalender import tag03_loesung as heute
except ImportError:
    from pyventskalender import tag03 as heute


class Tag03Tests(TestCase):

    def test_ich_mag(self):
        for tiere in ["Katzen", "katzen", "KaTzEn", "Hunde", "Vögel"]:
            expected = "Ich mag {}.".format(tiere.upper())
            self.assertEqual(heute.ich_mag(tiere), expected)

    def test_ich_will(self):
        for tiere in [("Katzen", "Hunde"), ("Fische", "Elche")]:
            for zahlen in [(3, 2), (7, 9)]:
                expected = "Ich mag {} {} und {} {}!.".format(
                    zahlen[0],
                    tiere[0].upper(),
                    zahlen[1],
                    tiere[1].upper()
                )
                self.assertEqual(heute.ich_will(zahlen[0], tiere[0], zahlen[1], tiere[1]), expected)

    def test_futterration_berechnen(self):
        for hamster, fische in [(2, 4), (3, 5), (0, 0), (100, 100)]:
            expected = heute.MASSE_FUTTER_FISCH_PRO_TAG_IN_G * fische + \
                       heute.MASSE_FUTTER_HAMSTER_PRO_TAG_IN_G * hamster
            self.assertEqual(heute.futterration_berechnen(hamster, fische), expected)
