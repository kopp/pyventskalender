from unittest import TestCase
from unittest.mock import patch
from io import StringIO

try:
    from pyventskalender import tag06_loesung as heute
except ImportError:
    from pyventskalender import tag06 as heute


def make_fake_input(replies, prompts):
    """
    Create a function to use as mock for `input` that will store the prompt
    (passed to `input`) in `prompts` and that returns the `replies` as
    `input` would return a reply the user types.
    """
    def fake_input(prompt):
        prompts.append(prompt)
        return replies.pop(0)
    return fake_input


class Tag06Tests(TestCase):

    def test_10_leere_liste_ist_da(self):
        self.assertTrue("unverstanden" in dir(heute),
                        msg="Ich konnte kein 'unverstanden' finden.")
        self.assertIs(type(heute.unverstanden), list)

    def test_20_frage_nach_lieblingstieren_einfach(self):
        prompts = []
        replies = ["A", "B", "C"]
        expected_replies = replies.copy()

        with patch('sys.stdout', new = StringIO()) as fake_out:
            with patch('builtins.input', make_fake_input(replies, prompts)):
                reply = heute.frage_nach_lieblingstieren()
                self.assertEqual(len(prompts), 3)
                for prompt in prompts:
                    self.assertEqual(prompt, "Nenne ein Lieblingstier:")
                self.assertEqual(fake_out.getvalue(), "")
                self.assertEqual(reply, expected_replies)

    def test_30_frage_nach_lieblingstieren_mehrere_antworten(self):
        prompts = []
        replies = ["A", "B", "A", "C"]
        expected_replies = ["A", "B", "C"]

        with patch('sys.stdout', new = StringIO()) as fake_out:
            with patch('builtins.input', make_fake_input(replies, prompts)):
                reply = heute.frage_nach_lieblingstieren()
                self.assertEqual(len(prompts), 4)
                for prompt in prompts:
                    self.assertEqual(prompt, "Nenne ein Lieblingstier:")
                self.assertEqual(fake_out.getvalue(), "A hattest du schon gesagt.\n")
                self.assertEqual(reply, expected_replies)

    def test_40_platz_auf_siegertreppchen(self):
        self.assertEqual(heute.platz_auf_siegertreppchen(["A", "B", "C"], "B"), 2)
        self.assertEqual(heute.platz_auf_siegertreppchen(["A", "B", "C"], "A"), 1)
        self.assertEqual(heute.platz_auf_siegertreppchen(["A", "B", "C"], "C"), 3)
        self.assertEqual(heute.platz_auf_siegertreppchen(["A", "B", "C"], "D"), None)
