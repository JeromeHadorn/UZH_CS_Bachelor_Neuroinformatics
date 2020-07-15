from unittest import TestCase
from public.script import survival_rates


class PublicTestSuite(TestCase):

    def test_example_data(self):
        actual = survival_rates((
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            [
                (True, '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38, 71.2833),
                (False, '3', 'Heikkinen Miss. Laina', 'female', 26, 7.925)
            ]
        ))
        expected = (
            (None, None),
            (None, 50.0)
        )
        self.assertEqual(expected, actual)