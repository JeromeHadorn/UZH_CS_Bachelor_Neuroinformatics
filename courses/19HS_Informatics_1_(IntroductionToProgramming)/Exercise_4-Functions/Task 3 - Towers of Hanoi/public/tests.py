from unittest import TestCase
from public.script import req_steps


class PublicTestSuite(TestCase):

    def test1(self):
        n = 10
        expected = 1023
        actual = req_steps(n)
        m = "The calculation is not correct for {} disks.".format(n)
        self.assertEqual(expected, actual, m)
