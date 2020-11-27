from unittest import TestCase
from os.path import exists, pardir, join, abspath, dirname
from os import environ

PROJEKT_ORDNER = abspath(join(dirname(__file__), pardir))
VENV_ORDNER = join(PROJEKT_ORDNER, "venv")

try:
    from pyventskalender import tag20_loesung as heute

    class Tag20Tests(TestCase):
        pass

except ImportError:
    from pyventskalender import tag20 as heute

    class Tag20Tests(TestCase):

        def test_10_venv_ordner_existiert(self):
            self.assertTrue(exists(VENV_ORDNER),
                            msg=f"venv Ordner existiert noch nicht; erwartet bei {VENV_ORDNER}")
            
        def test_20_virtual_env_aktiviert(self):
            aktives_virtual_environment = environ.get("VIRTUAL_ENV")
            self.assertIsNotNone(aktives_virtual_environment,
                                msg="Das Virtual env scheint nicht aktiviert zu sein")
            self.assertEqual(VENV_ORDNER, aktives_virtual_environment,
            msg=f"Das aktivierte Virtual Environment ist nicht an der erwarteten Stelle {VENV_ORDNER}")

        def test_30_cat_fact_installiert(self):
            try:
                import cat_fact
                import_funtioniert = True
            except ModuleNotFoundError:
                import_funtioniert = False
            self.assertTrue(import_funtioniert,
                            msg="Es war nicht möglich, cat_fact zu importieren.  Hast du es installiert?")


            

