from unittest import TestCase
from public.script import compress


class PublicTestSuite(TestCase):

    def test_1(self):
        actual = compress([
            {"a": 1, "b": 2, "c": 3},
            {"a": 4, "c": 6, "b": 5}
        ])
        expected = (
            ("a", "b", "c"),
            [
                (1, 2, 3),
                (4, 5, 6)
            ]
        )
        self.assertEqual(expected, actual)

    # This test suite does not exhaustively test the implementation,
    # a passing "test & run" does not mean that all possible cases
    # have been considered. For the grading, an extended tests suite
    # will be executed that will cover many more cases.

    # Feel free to add additional test cases here. All test cases
    # will be executed as part of the "test & run".
