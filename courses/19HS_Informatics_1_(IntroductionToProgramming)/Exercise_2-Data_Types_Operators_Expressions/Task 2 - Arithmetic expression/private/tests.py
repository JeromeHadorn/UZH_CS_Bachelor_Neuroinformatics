import builtins
import importlib
from unittest import TestCase


def set_vars(a, b, c, d):
    try: del script.a
    except: pass
    try: del script.b
    except: pass
    try: del script.c
    except: pass
    try: del script.d
    except: pass
    builtins.a = a
    builtins.b = b
    builtins.c = c
    builtins.d = d


set_vars(1,1,1,1)
from public import script


def exec(a, b, c, d):
    set_vars(a, b, c, d)
    importlib.reload(script)
    return script.res


class PrivateTestSuite(TestCase):

    def _test(self, a, b, c, d, expected):
        actual = exec(a, b, c, d)
        m = "@@Calculation not correct for a={}, b={}, c={}, d={}... expected result is {}!@@".format(a, b, c, d, expected)
        self.assertAlmostEqual(expected, actual, 5, m)

    def test_case1(self):
        self._test(1, 2, 3, 4, 1.444444)

    def test_case2(self):
        self._test(2, 3, 4, 5, 2.428571)

    def test_case3(self):
        self._test(3, 4, 5, 6, 3.432432)

    def test_case4(self):
        self._test(4, 5, 6, 7, 4.438596)
