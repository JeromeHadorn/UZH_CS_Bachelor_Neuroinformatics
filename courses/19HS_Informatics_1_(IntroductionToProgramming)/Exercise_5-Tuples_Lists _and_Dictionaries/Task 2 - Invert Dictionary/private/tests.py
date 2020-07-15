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
    from public.script import invert
except Exception:
    exception = sys.exc_info()[0]


from unittest import TestCase
class PrivateTestSuite(TestCase):

    def _assertType(self, expected, obj):
        if type(obj) != expected:
            m = "@@The return value of your function does not have the right type ({} vs. {}).@@".format(expected.__name__, type(obj).__name__)
            self.fail(m)

    def _assert(self, _in, expected, m=None):

        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        # try executing the code
        try:
            actual = invert(_in)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

        # make sure return type is correct
        self._assertType(dict, actual)

        if actual is _in:
            m = "@@Instead of mutating the provided dictionary, the implementation should create a new one.@@"
            self.fail(m)

        # prepare "default message", if none is provided
        if m == None:
            m = "@@Result is incorrect for input {}.@@".format(_in)

        # actual unit test
        self.assertEqual(expected, actual, m)


    def test_1(self):
        self._assert({}, {}, "@@Empty dictionaries are not handled correctly.@@")

    def test_2(self):
        self._assert({1:2}, {2:[1]})

    def test_3(self):
        self._assert({1:2, 3:2}, {2:[1, 3]})

    def test_4(self):
        self._assert({3:2, 1:2}, {2:[1, 3]}, "@@The lists of former keys are not sorted.@@")

