from io import StringIO 
from unittest import TestCase 
from unittest.mock import patch 
  
class Tag01Tests(TestCase): 
      
    def test_standard_output(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            from pyventskalender import tag01_loesung
            self.assertTrue(fake_out.getvalue().startswith("Hallo Welt"), msg="Es wird nicht der richtige Text ausgegeben -- verwende print('text') um 'text' auszugeben.")
