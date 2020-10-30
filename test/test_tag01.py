from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class Tag01Tests(TestCase):

    def test_standard_output(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            try:
                # Wenn die Loesungen da sind, importiere diese, damit man auch
                # bei Problemen in den vorangegangenen Tagen weiter machen
                # kann.
                from pyventskalender import tag01_loesung
            except ImportError:
                # Ist die Loesung nicht vorhanden, heisst das, dass sie noch
                # nicht heruntergeladen ist, also dass man die Aufgaben jetzt
                # selbst loesen muss.
                from pyventskalender import tag01
            self.assertTrue(fake_out.getvalue().startswith("Hallo Welt"),
                            msg="Es wird nicht der richtige Text ausgegeben"
                            " -- verwende print('text') um 'text' auszugeben.")
