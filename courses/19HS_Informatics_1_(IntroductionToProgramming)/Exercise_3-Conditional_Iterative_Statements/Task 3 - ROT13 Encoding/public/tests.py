import builtins
import importlib
from unittest import TestCase


builtins.plain_text = ""
builtins.shift_by = 0
from public import script


def rot(plain_text, shift_by):
    try: del script.plain_text
    except: pass
    try: del script.shift_by
    except: pass

    builtins.plain_text = plain_text
    builtins.shift_by = shift_by
    importlib.reload(script)
    return script.encoded


class PublicTestSuite(TestCase):

    def test_case0(self):
        actual = rot("a, B, c#!", 1)
        expected = "b, C, d#!"
        self.assertEqual(expected, actual)

    # feel free to extend the class with your own test cases

