import builtins
import importlib
from unittest import TestCase


def set_vars(a, b, c, d):
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


class PublicTestSuite(TestCase):

    def test_a_simple_order(self):
        actual = exec(1, 2, 3, 4)
        expected = 1.444444

        m = "Calculation not correct for a=1, b=2, c=3, d=4!"
        self.assertAlmostEqual(expected, actual, 5, m)
