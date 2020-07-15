from unittest import TestCase
from public.script import fac


class PublicTestSuite(TestCase):

    def test1(self):
         self.assertEqual(120, fac(5))
         self.assertEqual(6, fac(3))
