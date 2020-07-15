from unittest import TestCase
from public.script import Fridge


class PublicTestSuite(TestCase):

    def test_example(self):
        f = Fridge()
        # put an item into the fridge
        f.store((191112, "Butter"))
        self.assertEquals(1, len(f))
        # take it out again
        item = f.take((191112, "Butter"))
        self.assertEquals(0, len(f))
        # is it the right item?
        self.assertEquals((191112, "Butter"), item)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
