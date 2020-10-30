from unittest import TestCase
from unittest.mock import patch
from io import StringIO

try:
    from pyventskalender import tag07_loesung as heute
except ImportError:
    from pyventskalender import tag07 as heute


class Tag07Tests(TestCase):

    def test_kuehe_machen_muehe(self):
        self.assertEqual(heute.kuehe_machen_muehe(0), "0 Kühe machen keine Mühe")
        self.assertEqual(heute.kuehe_machen_muehe(1), "1 Kuh macht Muh")
        for kuehe in range(2, 10):
            expected = "{} Kühe machen {} mal Mühe".format(kuehe, kuehe)
            self.assertEqual(heute.kuehe_machen_muehe(kuehe), expected)

    def _assert_sinnspruch(self, anzahl_min: int, anzahl_max: int, expected_text: str):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            heute.kuh_sinnsprueche(anzahl_min, anzahl_max)
            self.assertEqual(fake_out.getvalue(), expected_text)

    def test_kuh_sinnsprueche(self):
        self._assert_sinnspruch(0, 0, "0 Kühe machen keine Mühe\n")
        self._assert_sinnspruch(1, 1, "1 Kuh macht Muh\n")
        self._assert_sinnspruch(2, 2, "2 Kühe machen 2 mal Mühe\n")
        self._assert_sinnspruch(1, 2, "1 Kuh macht Muh\n2 Kühe machen 2 mal Mühe\n")
        self._assert_sinnspruch(1, 3,
                                "1 Kuh macht Muh\n"
                                "2 Kühe machen 2 mal Mühe\n"
                                "3 Kühe machen 3 mal Mühe\n")
