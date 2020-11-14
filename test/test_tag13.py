from unittest import TestCase
from unittest.mock import patch
import re

try:
    from pyventskalender import tag13_loesung as heute
except ImportError:
    from pyventskalender import tag13 as heute


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

EXPECTED_RE = re.compile(r"(<.*?>)")

class Tag13Tests(TestCase):

    def find_in_text(self, text):
        self.assertIsNotNone(
            heute.EINZUSETZENDES_WORT_RE.search(text),
            msg="Teste deine Regular Expression mit '{}'".format(text)
        )
    
    def find_not_in_text(self, text):
        self.assertIsNone(
            heute.EINZUSETZENDES_WORT_RE.search(text),
            msg="Teste deine Regular Expression mit '{}' -- sollte nicht klappen".format(text)
        )

    def find_correct_groups(self, text):
        expected_groups = EXPECTED_RE.findall(text)
        groups = heute.EINZUSETZENDES_WORT_RE.findall(text)
        self.assertEqual(groups, expected_groups)

    def test_einzusetzendes_wort_re(self):
        for text in ["<x>", "a <x>", "<x> a", "<x> <y>", "a <x> <y>", "a <x> <y> b", "a <x> b <y> c"]:
            self.find_in_text(text)
        for text in ["a", "<b", "c>", ">a<"]:
            self.find_not_in_text(text)
        for text in ["<x>", "a <x>", "a <ü>", "a b c <d e> f <gh i> <j><k>"]:
            self.find_correct_groups(text)

    def mad_lib_durchlauf(self, text, replies):
        prompts = []

        expected_prompts = EXPECTED_RE.findall(text)

        expected_result = text
        for prompt, reply in zip(expected_prompts, replies):
            expected_result = expected_result.replace(prompt, reply)


        with patch('builtins.input', make_fake_input(replies, prompts)):
            ergebnis = heute.mad_libs(text)
            self.assertIsNone(
                EXPECTED_RE.search(ergebnis),
                msg="Es sollten keine zu ersetzenden Elemente mehr im Ergebnis {} sein".format(ergebnis)
            )
            self.assertEqual(len(prompts), len(expected_prompts),
                             msg="Es wurde nicht die richtige Zahl an zu ersetzenden Worten gefunden/den User gefragt; text war '{}'".format(text))
            for present, expected in zip(prompts, expected_prompts):
                self.assertIn(expected, present,
                              msg="Der erwartete Prompt ist nicht aufgetaucht")
            self.assertEqual(ergebnis, expected_result)

    def test_mad_libs(self):
        self.mad_lib_durchlauf(
            "a",
            []
        )
        self.mad_lib_durchlauf(
            "a <x>",
            ["y"]
        )
        self.mad_lib_durchlauf(
            "a <x> <y>",
            ["u", "v"]
        )
        self.mad_lib_durchlauf(
            "a <asdf asdf asdf x> <xxx xxx xxx>",
            ["abcde fghi", "jkl mno"]
        )
        self.mad_lib_durchlauf(
            "a <x> b <foo bar> c d <a b c - d> e",
            ["x-A", "foo bar-B", "a b c - d-C"]
        )