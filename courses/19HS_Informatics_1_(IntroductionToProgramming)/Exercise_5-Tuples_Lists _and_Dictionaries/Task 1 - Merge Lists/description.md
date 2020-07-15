
Write a function that expects two lists of integers, `a` and `b`, as parameters. The function should merge the elements of both lists by index and store them as tuples in a new list. If one list is shorter than the other, the last element of the shorter list should be repeated as often as necessary. If one of both lists is empty, the result should be the empty list.

Please consider the following example:

    merge([0, 1, 2], [5, 6]) -> [(0, 5), (1, 6), (2, 6)]

You can assume that the parameters are always valid lists and you do not need to provide any kind of input validation.

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail.


