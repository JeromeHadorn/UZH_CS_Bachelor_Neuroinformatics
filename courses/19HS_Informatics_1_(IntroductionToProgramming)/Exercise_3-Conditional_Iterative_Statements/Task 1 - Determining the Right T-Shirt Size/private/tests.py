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


DELTA = 0.0001
class PrivateTestSuite(TestCase):

    def _test(self, circumference, expected):
        actual = fun(circumference)
        m = "@@Determined size for a circumference of {} is not correct!@@".format(circumference)
        self.assertEqual(expected, actual, m)

    def test_XS_lower(self):
        self._test(80-DELTA, "N/A")

    def test_XS(self):
        self._test(80, "XS")

    def test_XS_higher(self):
        self._test(80+DELTA, "XS")

    def test_S_lower(self):
        self._test(90-DELTA, "XS")

    def test_S(self):
        self._test(90, "XS")

    def test_S_higher(self):
        self._test(90+DELTA, "S")

    def test_M_lower(self):
        self._test(98-DELTA, "S")

    def test_M(self):
        self._test(98, "S")

    def test_M_higher(self):
        self._test(98+DELTA, "M")

    def test_L_lower(self):
        self._test(104-DELTA, "M")

    def test_L(self):
        self._test(104, "M")

    def test_L_higher(self):
        self._test(104+DELTA, "L")

    def test_XL_lower(self):
        self._test(111-DELTA, "L")

    def test_XL(self):
        self._test(111, "L")

    def test_XL_higher(self):
        self._test(111+DELTA, "XL")

    def test_XXL_lower(self):
        self._test(124-DELTA, "XL")

    def test_XXL(self):
        self._test(124, "XL")

    def test_XXL_higher(self):
        self._test(124+DELTA, "N/A")
