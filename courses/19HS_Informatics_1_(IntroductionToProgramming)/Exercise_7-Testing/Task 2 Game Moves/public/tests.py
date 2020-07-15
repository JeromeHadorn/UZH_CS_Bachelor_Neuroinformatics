from unittest import TestCase
from script import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):


    def test_returnsAllPossibleDirections(self):
        pass

    def test_state_check_characters(self):
        state = (
                "#####   ",
                "###    #",
                "#   o ##",
                "   #####"
            )
        with self.assertRaises(Warning):
            move(state, "right")


    def test_state_check_sensibleSize_length(self):
        s1 = ("","","","","")
        with self.assertRaises(Warning):
            move(s1, "right")

    def test_state_check_sensibleSize_rows(self):
        s1 = ()
        with self.assertRaises(Warning):
            move(s1, "right")

    def test_state_check_linelength(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   ####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_state_check_onlyOnePlayer(self):
        state = (
            "##### o ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_move_state_oneMoveAtleastPossible(self):
        state = (
            "#####   ",
            "###  # #",
            "#   #o##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_move_state_oneMoveAtleastPossible_IncludingBorder(self):
        state = (
            "##### #o",
            "###  # #",
            "##  ####",
            "## #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_move_check_providedMoveisPossible(self):
        state = (
            "##### ##",
            "####o# #",
            "##  ####",
            "## #####"
        )
        with self.assertRaises(Warning):
            move(state, "right")
    def test_move_down(self):
        state = ("#####   ", "###    #", "#   o ##", "########")
        dire = 'down'
        self.assertRaises(Warning, move, state, dire)

    def test_move_up(self):
        state = ("#####   ", "########", "#   o ##", "########")
        dire = 'up'
        self.assertRaises(Warning, move, state, dire)

    def test_move_left(self):
        state = ("#####   ", "###    #", "#  #o ##", "########")
        dire = 'left'
        self.assertRaises(Warning, move, state, dire)

    def test_move_right(self):
        state = ("#####   ", "###    #", "#   o###", "########")
        dire = 'right'
        self.assertRaises(Warning, move, state, dire)
    def test_characters1(self):
        state = ("##?##   ", "###    #", "#   o ##", "   #####")
        dire = 'up'
        self.assertRaises(Warning, move, state, dire)

    def test_characters2(self):
        state = ("#####xxx", "#␣#xxxx#", "#xxxox##", "xxx#####")
        dire = 'up'
        self.assertRaises(Warning, move, state, dire)
    def test_provided_example(self):
        state = (
            "#####   ",
            "###    #",
            "# o   ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#  o  ##",
                "   #####"
            ),
            ("left", "right","up")
        )
        self.assertEqual(expected, actual)