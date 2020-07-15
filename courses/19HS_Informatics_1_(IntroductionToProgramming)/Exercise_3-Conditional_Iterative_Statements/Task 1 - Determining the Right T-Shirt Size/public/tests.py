import builtins
import importlib
from unittest import TestCase

builtins.circumference = 0
from public import script


def fun(circumference):
    try: del script.circumference
    except: pass
    builtins.circumference = circumference
    importlib.reload(script)
    return script.size


class PublicTestSuite(TestCase):

    def test_XS_lower(self):
        actual = fun(87.25)
        expected = "XS"
        self.assertEqual(expected, actual)

    # feel free to extend the class with your own test cases
