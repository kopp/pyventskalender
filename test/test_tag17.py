from pyventskalender.tag17 import Katze
from unittest import TestCase
from unittest.mock import patch, call

try:
    from pyventskalender import tag17_loesungX as heute
except ImportError:
    from pyventskalender import tag17 as heute


class Tag17Tests(TestCase):

    def test_10_mock_funktioniert(self):
        with patch.object(heute.Katze, 'macht_ton', return_value="X") as mock:
            katze = heute.Katze("Y")
            self.assertEqual(katze.macht_ton(), "X")
            mock.assert_has_calls([call()])

    def test_20_katzenkonzert_von(self):
        with patch.object(heute.Katze, 'macht_ton', return_value="Miau") as mock:
            katzen = [heute.Katze("Y"), heute.Katze("Z")]
            konzert = heute.katzenkonzert_von(katzen)
            self.assertEqual(konzert, "Miau Miau ")
            mock.assert_has_calls([call(), call()])

    def test_30_macht_ton_mit_namen(self):
        name = "Katzenname"
        katze = heute.Katze(name)
        ton = katze.macht_ton()
        self.assertIn(name, ton)
        self.assertIn("macht", ton)
        self.assertIn("Miauuuuu", ton)

    def test_40_katze_frisst(self):
        name = "Katzenname"
        katze = heute.Katze(name)
        self.assertIn('frisst', dir(katze),
                      msg="Katze hat noch keine Methode frisst")
        essen = "Brot"
        output = katze.frisst(essen)
        self.assertEqual(output, f"{name} mag {essen}")
        self.assertIn(essen, katze.magen)

    def test_50_katze_magen(self):
        name = "Katzenname"
        katze = heute.Katze(name)
        self.assertEqual(katze.magen, [],
                         msg="Katze sollte direkt bei Erschaffung mit magen ausgestattet werden.")
        gegessen = []
        for essen in ["Brot", "Maus", "Käse"]:
            self.assertEqual(katze.magen, gegessen)
            katze.frisst(essen)
            gegessen.append(essen)
            self.assertEqual(katze.magen, gegessen)
