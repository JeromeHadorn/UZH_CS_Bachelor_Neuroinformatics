import builtins
import importlib
from unittest import TestCase


def set_vars(plain_text, shift_by):
    try: del script.plain_text
    except: pass
    try: del script.shift_by
    except: pass

    builtins.plain_text = plain_text
    builtins.shift_by = shift_by


set_vars("", 0)
from public import script


def rot(plain_text, shift_by):
    set_vars(plain_text, shift_by)
    importlib.reload(script)
    return script.encoded


class PrivateTestSuite(TestCase):

    def _assert(self, plain_text, shift_by, expected, msg):
        actual = rot(plain_text, shift_by)
        if not msg:
            msg = "@@ROT{} of '{}' should be '{}', but was '{}'.@@".format(shift_by, plain_text, expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_case0(self):
        self._assert("", 1, "", "The encoding does not work for empty strings")

    def test_case1(self):
        self._assert("abzAZ!", 1, "bcaBA!", None)

    def test_case2(self):
        self._assert("abzAZ!", -1, "zayZY!", None)

    def test_case3(self):
        self._assert("abzAZ!", 0, "abzAZ!", None)

    def test_case4(self):
        self._assert("abzAZ!", 26, "abzAZ!", None)

    def test_case5(self):
        self._assert("abzAZ!", -26, "abzAZ!", None)

    def test_case6(self):
        self._assert("abzAZ!", 27, "bcaBA!", None)

    def test_case7(self):
        self._assert("abzAZ!", -27, "zayZY!", None)

    def test_case8(self):
        self._assert("abzAZ!", 2, "cdbCB!", None)

    def test_case9(self):
        self._assert("abzAZ!", 3, "decDC!", None)

    def test_case10(self):
        for ord in range(128):
            c = chr(ord)
            if c.isalpha():
                e = rot(c, 1)
                m = "@@After the encoding, some letters have become non-letters.@@"
                self.assertTrue(e.isalpha(), m)
                m = "@@Some letters do not get encoded.@@"
                self.assertNotEqual(c, e, m)

    def test_case11(self):
        for ord in range(128):
            c = chr(ord)
            if not c.isalpha():
                e = rot(c, 1)
                m = "@@Some non-letters get encoded.@@"
                self.assertEqual(c, e, m)
