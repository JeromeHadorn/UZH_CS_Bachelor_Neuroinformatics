from unittest import TestCase
from public.script import fac


class PrivateTestSuite(TestCase):

    def _assert_fac(self, n, expected):
        actual = fac(n)
        m = "@@The calculation of fac({}) is not correct!@@".format(n)
        self.assertEqual(expected, actual, m)

    def test0(self):
        self._assert_fac(0, 1)

    def test1(self):
        self._assert_fac(1, 1)

    def test2(self):
        self._assert_fac(2, 2)

    def test3(self):
        self._assert_fac(3, 6)

    def test4(self):
        self._assert_fac(4, 24)

    def test6(self):
        self._assert_fac(6, 720)

    def test10(self):
        self._assert_fac(10, 3628800)

    def test18(self):
        self._assert_fac(18, 6402373705728000)
