from unittest import TestCase
from script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEquals(expected, actual)

    def test_example2(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abcdefghiMastarDjklmno"
        actual = f.filter(msg)
        expected = "abcdefghi?#$?#$?jklmno"
        self.assertEquals(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
