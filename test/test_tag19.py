from unittest import TestCase
from unittest.mock import patch, call

try:
    from pyventskalender import tag19_loesung as heute
except ImportError:
    from pyventskalender import tag19 as heute


class Tag19Tests(TestCase):

    def test_10_zufaelliges_neues_satzglied(self):
        satzglied = heute.Satzglied(list("abcdefghijk"))
        self.assertIn("zufaelliges_neues", dir(satzglied))
        verschiedene_texte = set()
        for _ in range(50):
            satzglied.zufaelliges_neues()
            verschiedene_texte.add(satzglied.text)
        self.assertGreater(len(verschiedene_texte), 2,
                           msg=f"Bei 50 wiederholungen von zufaelliges_neues gab es nur {len(verschiedene_texte)} verschiedene Ausgaben: {verschiedene_texte} -- das ist sehr suspekt")

    def test_20_zufaelligen_neuen_satz(self):
        satz = heute.Satz()
        self.assertIn("zufaelligen_neuen", dir(satz))
        with patch.object(heute.Satzglied, "zufaelliges_neues", return_value="X") as mock:
            satz.zufaelligen_neuen()
            mock.assert_has_calls([call(), call(), call(), call()])

    def test_30_str_bei_satz(self):
        satz = heute.Satz()
        satz.adverbiale.text = "Adverbiale"
        satz.verb.text = "Verb"
        satz.subjekt.text = "Subjekt"
        satz.objekt.text = "Objekt"
        self.assertEqual(str(satz), "Adverbiale Verb Subjekt Objekt.")