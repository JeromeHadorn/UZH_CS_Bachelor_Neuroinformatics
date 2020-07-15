# replace input implementation
import builtins, sys
class YouCannotUseInputInACCESSException(Exception): pass
def crashing_input(prompt):
    raise YouCannotUseInputInACCESSException("You cannot use 'input' in the grading environment.")
builtins.input_orig = builtins.input
builtins.input = crashing_input

# catch potential exception from import
exception = None
try:
    from public.script import survival_rates
except Exception:
    exception = sys.exc_info()[0]

# some utility functions
def youngMale(has_survived):
    return (has_survived, 1, "Some Name", "male", 15.0, 1.23)

def oldMale(has_survived):
    return (has_survived, 1, "Some Name", "male", 16.0, 1.23)

def youngFemale(has_survived):
    return (has_survived, 1, "Some Name", "female", 15.0, 1.23)

def oldFemale(has_survived):
    return (has_survived, 1, "Some Name", "female", 16.0, 1.23)

def my_round(survivors, total):
    perc = 100*(survivors/total)
    return round(perc, 1)


from unittest import TestCase
class PrivateTestSuite(TestCase):

    # assert that obj has the expected type
    def _assertType(self, expected, obj, m=None):
        if type(obj) != expected:
            if not m:
                m = "@@The return value of your function does not have the right type ({} vs. {}).@@".format(expected.__name__, type(obj).__name__)
            self.fail(m)

    # try executing the code, fails gracefully
    def _exec(self, _in):
        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        # add header and execute
        _in = (
            ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
            _in
        )

        try:
            actual = survival_rates(_in)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

        # make sure return type is correct
        self._assertType(tuple, actual, "@@Unexpected return value: The result is not a tuple.@@")
        self.assertEqual(2, len(actual), "@@Unexpected return value: The resulting tuple does not have 2 elements.@@")
        self._assertType(tuple, actual[0], "@@Unexpected return value: The resulting tuple should contain nested tuples.@@")
        self.assertEqual(2, len(actual[0]), "@@Unexpected return value: The nested tuple should have size 2.@@")
        self._assertType(tuple, actual[1], "@@Unexpected return value: The resulting tuple should contain nested tuples.@@")
        self.assertEqual(2, len(actual[1]), "@@Unexpected return value: The nested tuple should have size 2.@@")
        return actual

    def _assert(self, _in, expected, m=None):
        actual = self._exec(_in)

        # prepare "default message", if none is provided
        if not m:
            m = "@@The calculation is not correct for input:\n{}@@".format(_in)

        # actual unit test
        self.assertEqual(expected, actual, m)

    def test0a_check_for_None(self):
        actual = self._exec([youngMale(True)])
        yf = actual[0][1] is not None
        om = actual[1][0] is not None
        of = actual[1][1] is not None
        if yf or om or of:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0b_check_for_None(self):
        actual = self._exec([youngFemale(True)])
        ym = actual[0][0] is not None
        om = actual[1][0] is not None
        of = actual[1][1] is not None
        if ym or om or of:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0c_check_for_None(self):
        actual = self._exec([oldMale(True)])
        ym = actual[0][0] is not None
        yf = actual[0][1] is not None
        of = actual[1][1] is not None
        if ym or yf or of:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0d_check_for_None(self):
        actual = self._exec([oldFemale(True)])
        ym = actual[0][0] is not None
        yf = actual[0][1] is not None
        om = actual[1][0] is not None
        if ym or yf or om:
            self.fail("@@Parts that do not have any values, should be set to None.@@")

    def test0e_rounded_not_multiplied(self):
        actual = self._exec([youngMale(False), youngMale(False), youngMale(True)])
        if type(actual[0][0]) == float and actual[0][0] == 0.3:
            self.fail("@@The implementation does not multiply the results by 100 to get percentages.@@")

    def test0e_not_rounded_not_multiplied(self):
        actual = self._exec([youngMale(False), youngMale(False), youngMale(True)])
        if type(actual[0][0]) == float and actual[0][0] > 0.3 and actual[0][0] < 0.34:
            self.fail("@@The implementation does not multiply the results by 100 to get percentages.@@")

    def test0g_not_rounded_multiplied(self):
        actual = self._exec([youngMale(False), youngMale(False), youngMale(True)])
        if type(actual[0][0]) == float and actual[0][0] > 33.3 and actual[0][0] < 33.4:
            self.fail("@@The implementation does not round percentages to one decimal digit.@@")

    def test0h_incorrectly_rounded_not_multiplied(self):
        actual = self._exec([youngMale(False), youngMale(False), youngMale(True)])
        if actual[0][0] == 0:
            self.fail("@@The implementation is either incorrect or it does not multiply the results by 100 to get percentages.@@")

    def test0i_incorrectly_rounded_multiplied(self):
        actual = self._exec([youngMale(False), youngMale(False), youngMale(True)])
        if actual[0][0] == 33:
            self.fail("@@The rounding should preserve one decimal digit, instead, the implementation rounds to an int.@@")

    def test1a_young_male_all(self):
        self._assert([
            youngMale(True)
        ], (
            (100.0, None),
            (None, None)
        ), "@@The survival rate of male passengers who are 15 and younger is not correct when all survived.@@")

    def test1b_young_male_none(self):
        self._assert([
            youngMale(False)
        ], (
            (0.0, None),
            (None, None)
        ), "@@The survival rate of male passengers who are 15 and younger is not correct when nobody survived.@@")

    def test1c_young_male_some(self):
        self._assert([
            youngMale(False),
            youngMale(False),
            youngMale(True)
        ], (
            (33.3, None),
            (None, None)
        ), "@@The survival rate of male passengers who are 15 and younger is not correct.@@")

    def test2a_young_female_all(self):
        self._assert([
            youngFemale(True)
        ], (
            (None, 100.0),
            (None, None)
        ), "@@The survival rate of female passengers who are 15 and younger is not correct when all survived.@@")

    def test2b_young_female_none(self):
        self._assert([
            youngFemale(False)
        ], (
            (None, 0.0),
            (None, None)
        ), "@@The survival rate of female passengers who are 15 and younger is not correct when nobody survived.@@")

    def test2c_young_female_some(self):
        self._assert([
            youngFemale(False),
            youngFemale(False),
            youngFemale(True)
        ], (
            (None, 33.3),
            (None, None)
        ), "@@The survival rate of female passengers who are 15 and younger is not correct.@@")

    def test3a_old_male_all(self):
        self._assert([
            oldMale(True)
        ], (
            (None, None),
            (100.0, None)
        ), "@@The survival rate of male passengers who are older than 15 is not correct when all survived.@@")

    def test3b_old_male_none(self):
        self._assert([
            oldMale(False)
        ], (
            (None, None),
            (0.0, None)
        ), "@@The survival rate of male passengers who are older than 15 is not correct when nobody survived.@@")

    def test3c_old_male_some(self):
        self._assert([
            oldMale(False),
            oldMale(False),
            oldMale(True)
        ], (
            (None, None),
            (33.3, None)
        ), "@@The survival rate of male passengers who are older than 15 is not correct.@@")

    def test4a_old_female_all(self):
        self._assert([
            oldFemale(True)
        ], (
            (None, None),
            (None, 100.0)
        ), "@@The survival rate of female passengers who are older than 15 is not correct when all survived.@@")

    def test4b_old_female_none(self):
        self._assert([
            oldFemale(False)
        ], (
            (None, None),
            (None, 0.0)
        ), "@@The survival rate of female passengers who are older than 15 is not correct when nobody survived.@@")

    def test4c_old_female_some(self):
        self._assert([
            oldFemale(False),
            oldFemale(False),
            oldFemale(True)
        ], (
            (None, None),
            (None, 33.3)
        ), "@@The survival rate of female passengers who are older than 15 is not correct.@@")

    def test5a_integrated_example(self):
        self._assert([
            youngMale(True),
            youngMale(False),
            youngMale(False),
            #
            youngFemale(True),
            youngFemale(False),
            youngFemale(False),
            youngFemale(False),
            #
            oldMale(True),
            oldMale(False),
            oldMale(False),
            oldMale(False),
            oldMale(False),
            #
            oldFemale(True),
            oldFemale(False),
            oldFemale(False),
            oldFemale(False),
            oldFemale(False),
            oldFemale(False),
        ], (
            (my_round(1, 3), my_round(1, 4)),
            (my_round(1, 5), my_round(1, 6))
        ), "@@An integrated example that fills all quadrants is not correctly calculated.@@")

    def test5a_integrated_example(self):
        self._assert([
            youngMale(True),
            youngMale(False),
            #
            youngFemale(True),
            youngFemale(True),
            youngFemale(False),
            #
            oldMale(True),
            oldMale(True),
            oldMale(True),
            oldMale(False),
            #
            oldFemale(True),
            oldFemale(True),
            oldFemale(True),
            oldFemale(True),
            oldFemale(False),
        ], (
            (my_round(1, 2), my_round(2, 3)),
            (my_round(3, 4), my_round(4, 5))
        ), "@@An integrated example that fills all quadrants is not correctly calculated.@@")

    def test_rounding_is_correct(self):
        self._assert([
            youngMale(False),
            youngMale(True),
            youngMale(True),
            #
            youngFemale(False),
            youngFemale(True),
            youngFemale(True),
            #
            oldMale(False),
            oldMale(True),
            oldMale(True),
            #
            oldFemale(False),
            oldFemale(True),
            oldFemale(True)
        ], (
            (66.7, 66.7),
            (66.7, 66.7)
        ), "@@The rounding of survival rates is not correct, 66.666... should be rounded to 66.7.@@")