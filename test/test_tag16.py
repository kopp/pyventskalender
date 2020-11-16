from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import re

try:
    from pyventskalender import tag16_loesung as heute
except ImportError:
    from pyventskalender import tag16 as heute


class RepliesExhausted(Exception):
    pass


def make_fake_input(replies, prompts):
    """
    Create a function to use as mock for `input` that will store the prompt
    (passed to `input`) in `prompts` and that returns the `replies` as
    `input` would return a reply the user types.
    """
    def fake_input(prompt):
        prompts.append(prompt)
        if len(replies) == 0:
            raise RepliesExhausted
        return replies.pop(0)
    return fake_input

EXPECTED_RE = re.compile(r"(<.*?>)")

class Tag16Tests(TestCase):

    def test_10_aufgeben(self):

        replies = ["ich gebe auf"]
        prompts = []

        with patch('builtins.input', make_fake_input(replies, prompts)):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                wort = "asdfasdfasdf"
                heute.galgenmannspiel(wort)
                ausgegebener_text = fake_out.getvalue()
                self.assertTrue(ausgegebener_text.startswith("Gesucht:"))
                self.assertIn("Ok. Das Wort wäre gewesen:", ausgegebener_text)
                self.assertIn(wort, ausgegebener_text)

    def test_20_genau_einen_buchstaben(self):

        replies = ["xxx", "x"]
        prompts = []

        with patch('builtins.input', make_fake_input(replies, prompts)):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                wort = "asdfasdfasdf"
                try:
                    heute.galgenmannspiel(wort)
                except RepliesExhausted:
                    # If we enter the infinite loop, we abort it by raising
                    # this exception
                    pass
                ausgegebener_text = fake_out.getvalue()
                self.assertTrue(ausgegebener_text.startswith("Gesucht:"))
                self.assertIn("Bitte genau einen Buchstaben angeben", ausgegebener_text)
                self.assertNotIn(wort, ausgegebener_text)

    def test_30_galgenmannspiel_gewonnen(self):
        wort = "AAbbAaBb"
        replies = ["a", "x", "y", "b"]
        prompts = []

        with patch('builtins.input', make_fake_input(replies, prompts)):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                ergebnis = heute.galgenmannspiel(wort)
                self.assertTrue(ergebnis)
                ausgegebener_text = fake_out.getvalue()
                self.assertNotIn("Ok. Das Wort wäre gewesen:", ausgegebener_text)
                self.assertNotIn("Bitte genau einen Buchstaben angeben", ausgegebener_text)
                self.assertIn("x ist leider falsch; bisher falsch geraten: ['x']", ausgegebener_text)
                self.assertIn("y ist leider falsch; bisher falsch geraten: ['x', 'y']", ausgegebener_text)
                self.assertIn(wort, ausgegebener_text)
                self.assertIn("Erraten", ausgegebener_text)

    def test_40_galgenmannspiel_verloren(self):
        wort = "AAbbAaBb"
        replies = 100 * ["x"]
        prompts = []

        with patch('builtins.input', make_fake_input(replies, prompts)):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                ergebnis = heute.galgenmannspiel(wort)
                self.assertFalse(ergebnis,
                                 msg=f"Ich muss verlieren, wenn ich immer nur x eingebe aber {wort} gesucht ist.")
                ausgegebener_text = fake_out.getvalue()
                self.assertIn(wort, ausgegebener_text)
                self.assertNotIn("Erraten", ausgegebener_text)
                self.assertIn("Leider nicht geklappt", ausgegebener_text)
