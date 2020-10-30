from unittest import TestCase

try:
    from pyventskalender import tag08_loesung as heute
except ImportError:
    from pyventskalender import tag08 as heute


class Tag08Tests(TestCase):
    NICHTSAEUGER = ["Eidechse", "Frosch", "Ente", "Vogel"]

    def _teste_tierset(self, tier_tags):
        """
        Ein Tiertag besteht aus (s|n)(index)
        s - Säuger
        n - Nichtsäuger
        index: Index in Liste
        """
        tiere = []
        saeugetiere = []
        for tag in tier_tags:
            index = int(tag[1:])
            if tag.startswith("s"):
                tiere.append(heute.BEKANNTE_SAEUGETIERE[index])
                saeugetiere.append(heute.BEKANNTE_SAEUGETIERE[index])
            if tag.startswith("n"):
                tiere.append(Tag08Tests.NICHTSAEUGER[index])
        hoffentlich_saeugetiere = heute.saeugetiere_aus(tiere)
        self.assertEqual(hoffentlich_saeugetiere, saeugetiere)

    def test_saeugetiere_aus(self):
        heute.BEKANNTE_SAEUGETIERE
        self._teste_tierset(["s0"])
        self._teste_tierset(["n0"])

    def test_mensch_mag_tier(self):
        self.assertEqual(
            heute.mensch_mag_tier(
                ["Peter", "Paul"], ["Schweine", "Katzen"]
            ), ["Peter mag Schweine", "Peter mag Katzen", "Paul mag Schweine", "Paul mag Katzen"]
        )

        self.assertEqual(heute.mensch_mag_tier([], []), [])
        self.assertEqual(heute.mensch_mag_tier(["a"], ["x"]), ["a mag x"])
        self.assertEqual(heute.mensch_mag_tier(["a", "b", "c"], ["x"]), ["a mag x", "b mag x", "c mag x"])
