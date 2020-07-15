import builtins
import importlib
from unittest import TestCase


builtins.s = "a:b"
from public import script


def exec(s):
    try: del script.s
    except: pass
    builtins.s = s
    importlib.reload(script)
    return script.res


class PrivateTestSuite(TestCase):

    def _test(self, s, expected, m):
        actual = exec(s)
        if not m:
            m = "@@The program did not correctly transform \"{}\" into \"{}\"!@@".format(s, expected)
        self.assertEqual(expected, actual, m)

    def test_case1(self):
        self._test(":", ":", "Also \":\" is a correct input example, your transformation of it is not correct though!")

    def test_case2(self):
        self._test("A:", "a:",None)

    def test_case3(self):
        self._test(":b", ":B",None)

    def test_case4(self):
        self._test("aA:bB", "aa:BB",None)

    def test_case5(self):
        self._test("aAa:BbBb", "aaa:BBBB",None)

