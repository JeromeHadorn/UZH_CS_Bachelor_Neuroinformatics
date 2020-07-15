import builtins
import importlib
from unittest import TestCase


def set_vars(name, age):
    builtins.name = name
    builtins.age = age


set_vars("", -1)
from public import script


def exec(name, age):
    set_vars(name, age)
    importlib.reload(script)
    return script.greeting


class PublicTestSuite(TestCase):

    def test_basic(self):
        actual = exec("Hans", 37)
        expected = "Hello Hans, you are 37 years old!"

        m = "Hans (37) has not been greeted correctly!"
        self.assertEqual(expected, actual, m)
