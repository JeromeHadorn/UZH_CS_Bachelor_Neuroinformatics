from unittest import TestCase
from public.script import sort

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class SortTests(TestCase):


    def test_make_sure_returns_new_List(self):
        input = [5, 4, 3, 2, 1]
        actual = sort(input)
        self.assertFalse(input is actual)

    def test_unchanged(self):
        actual = [4, 3, 2, 1]
        sort(actual)
        expected = [4, 3, 2, 1]
        self.assertEqual(expected, actual)

    def test_none_if_input_none(self):
        input = None
        try:
            actual = sort(input)
        except:
            actual = -1
        expected = None
        self.assertEqual(expected, actual)

    def test_none_if_noneIterable(self):
        input = 212121212
        try:
            actual = sort(input)
        except:
            actual = -1
        expected = None
        self.assertEqual(None, actual)


    def test_check_list_int(self):
        input = [5, 4, 3, 2, 1]
        actual = sort(input)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, actual)


    def test_check_list_string(self):
        input = ["a", "z", "b"]
        actual = sort(input)
        expected = ["a", "b", "z"]
        self.assertEqual(expected, actual)

    def test_check_string(self):
        input = "world"
        actual = sort(input)
        expected = ['d', 'l', 'o', 'r', 'w']
        self.assertEqual(expected, actual)

