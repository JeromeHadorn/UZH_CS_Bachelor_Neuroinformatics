
Write a function `invert` that expects a dictionary `d`. The function should invert the mapping
of the dictionary and switch keys and values. Given that multiple keys might point to the same value, the inverted
dictionary has lists as values, in which all keys are collected *and sorted*.

Please consider the following example.

    invert({"a":1, "b":1, "c":3}) -> {1:["a", "b"], 3:["c"]}

You can assume that the parameter is always a dictionary and you do not need to provide any kind of input validation.
The implementation should not change the provided dictionary and create a new one instead.

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail.

**Note:** You are allowed to use the built-in function `sorted` to sort the list of previous keys.
