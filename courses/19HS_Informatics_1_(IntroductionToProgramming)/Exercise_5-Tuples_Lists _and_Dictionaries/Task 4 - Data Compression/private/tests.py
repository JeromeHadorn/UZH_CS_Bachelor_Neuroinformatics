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
    from public.script import compress
except Exception:
    exception = sys.exc_info()[0]


from unittest import TestCase
class PrivateTestSuite(TestCase):

    # assert that obj has the expected type
    def _assertType(self, expected, obj, m=None):
        if type(obj) != expected:
            if m == None:
                m = "@@The return value of your function does not have the right type ({} vs. {}).@@".format(expected.__name__, type(obj).__name__)
            self.fail(m)

    def _assert(self, _in, expected, m=None):

        # abort execution, when import did not work
        if exception != None:
            m = "@@Could not import solution for testing: {}@@".format(exception.__name__)
            self.fail(m)

        # try executing the code
        try:
            actual = compress(_in)
        except:
            exceptionType = sys.exc_info()[0]
            m = "@@Could not execute the solution for testing: {}@@".format(exceptionType.__name__)
            self.fail(m)

        # make sure return type is correct
        self._assertType(tuple, actual)

        # make sure the size of the tuple is two
        if len(actual) != 2:
            m = "@@Your result is a tuple, but it does not have the expected two elements (tuple of keys, list of value tuples).@@"
            self.fail(m)

        # make the two tuple elements have the right types
        self._assertType(tuple, actual[0], "@@The first element in your resulting tuple should be a tuple as well.@@")
        self._assertType(list, actual[1], "@@The second element in your resulting tuple should be a list.@@")



        # prepare "default message", if none is provided
        if m == None:
            m = "@@The compression did not work correctly for: {}@@".format(_in)

        # actual unit test
        self.assertEqual(expected, actual, m)


    def test_empty_list(self):
        self._assert([], ((), []))

    def test_empty_dictionary(self):
        self._assert([{}], ((), [()]))

    def test_1(self):
        self._assert([{1:2}], ((1,), [(2,)]))

    def test_2(self):
        self._assert([{1:2}, {1:3}], ((1,), [(2,), (3,)]))

    def test_3(self):
        self._assert([{1:2, 3:4}, {1:3, 3:5}], ((1, 3), [(2, 4), (3, 5)]))

    def test_3(self):
        self._assert([{1:2, 3:4}, {3:5, 1:3}], ((1, 3), [(2, 4), (3, 5)]), "@@Make sure that the values in the tuples stay consistent with the keys.@@")

    def test_ordering_of_keys(self):
        self._assert([{3:4, 1:2}, {1:3, 3:5}], ((1, 3), [(2, 4), (3, 5)]), "@@The keys are not ordered.@@")
