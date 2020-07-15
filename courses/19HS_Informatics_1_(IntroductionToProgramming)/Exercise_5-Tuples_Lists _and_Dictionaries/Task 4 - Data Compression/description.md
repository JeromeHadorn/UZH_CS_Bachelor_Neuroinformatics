


Dictionaries present a convenient way to group related information and to make them
easy to access. However, they take more memory, because the keys have to be stored
multiple times. They are also less convenient to use in data analysis tasks, for
example, they cannot be automatically sorted. In this task you will transform a
dictionary-based representation to a tuple-based representation that solves both of
these issues.

Assume you get a list of dictionaries that all have the same keys. For example:

    [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "c": 6, "b": 5}, # the order of keys is not fixed...
        ...
    ]

Your task is to transform this list of dictionaries into a representation that is more memory
efficient and easier to work with. Write a function `compress` that takes such a list of
dictionaries, extracts all keys, sorts them, and stores them in a tuple. This tuple should
then be used to transform the list of dictionaries into a list of tuples. Finally, the
function should return a tuple that contains both the keys and the resulting list of tuples.

More specifically, when called on the previous example, your function should return the following data:

    (
        ("a", "b", "c"),
        [
            (1, 2, 3),
            (4, 5, 6) # ... but the result should still be consistent with the keys!
        ]
    )


You can assume that the provided parameter is always a valid list of dictionaries and that
all these dictionaries in the list share the same keys. However, the order of the keys might
be different among the dictionaries. Make sure that your solution also works for empty lists
or for empty dictionaries.
 
**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail.

**Note:** Tuples are immutable, so you cannot append values. However, you can
use a `list` and `append` each record. The final result can then be converted to a
tuple. For example, `tuple([1, 2, 3])` is equivalent to `(1, 2, 3)`.

