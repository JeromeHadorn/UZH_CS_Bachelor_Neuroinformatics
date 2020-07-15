from unittest import TestCase
from public.script import read_csv


class PublicTestSuite(TestCase):

    def test_example_data(self):
        actual = read_csv("public/example.csv")
        expected = [
            ('Age', 'Gender', 'Weight (kg)', 'Height (cm)'),
            ('28', 'Female', '58', '168'),
            ('33', 'Male', '', '188')]
        self.assertEqual(expected, actual)
