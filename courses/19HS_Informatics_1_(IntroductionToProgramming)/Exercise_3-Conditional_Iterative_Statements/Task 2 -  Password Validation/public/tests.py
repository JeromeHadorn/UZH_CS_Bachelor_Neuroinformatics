import builtins
import importlib
from unittest import TestCase

builtins.pwd = ""
from public import script


def is_valid(pwd):
    try: del script.pwd
    except: pass
    builtins.pwd = pwd
    importlib.reload(script)
    return script.is_valid


class PublicTestSuite(TestCase):

    def test_valid1(self):
        self.assertTrue(is_valid("j-9F+d4K"))

    # feel free to extend the class with your own test cases
