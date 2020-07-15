import builtins
import importlib
from unittest import TestCase


def set_vars(name, age):
    try: del script.name
    except: pass
    try: del script.age
    except: pass
    builtins.name = name
    builtins.age = age


set_vars("", -1)
from public import script


def exec(name, age):
    set_vars(name, age)
    importlib.reload(script)
    return script.greeting


class PrivateTestSuite(TestCase):

    def _test(self, name, age):
        expected = "Hello {}, you are {} years old!".format(name, age)
        actual = exec(name, age)

        m = "@@{} ({}) has not been greeted correctly!@@".format(name, age)
        self.assertEqual(expected, actual, m)

    def test_case1(self):
        self._test("Hans", 37)

    def test_case2(self):
        self._test("Peter", 13)

    def test_case3(self):
        self._test("Sarah", 65)

    def test_case4(self):
        self._test("Julia", 8)
