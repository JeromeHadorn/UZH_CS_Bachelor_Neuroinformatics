import builtins
import importlib
from unittest import TestCase

builtins.s = "a:b"
from public import script


def exec(s):
    builtins.s = s
    importlib.reload(script)
    return script.res


class PublicTestSuite(TestCase):

    def test_basic(self):
        actual = exec("aB:cD")
        expected = "ab:CD"

        m = "This is not correct!"
        self.assertEqual(expected, actual, m)
