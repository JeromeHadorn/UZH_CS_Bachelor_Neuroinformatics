from unittest import TestCase
from public.script import preprocess


class PublicTestSuite(TestCase):

    def test_example(self):
        actual = preprocess([
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
            ('Dead', '3', 'Braund Ms. Maria', 'Female', '21', ''),
            ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
            ('', '3', 'Vander Planke Miss. Augusta', 'female', '', ''),
            ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')])
        expected = (
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            [
                (False, 3, 'Braund Mr. Owen Harris', 'male', 22.0, 7.25),
                (False, 3, 'Braund Ms. Maria', 'female', 21.0, 25.0),
                (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'female', 38.0, 71.28)
            ]
        )
        self.assertEqual(expected, actual)