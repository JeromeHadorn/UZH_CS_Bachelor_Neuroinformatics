# String operations

You have learned in the lecture how to use the string slicing operator to select substrings from a given string.
Strings also have very useful methods, like `find`, which can be used to find the index of a particular character
in a string (e.g., `"abc".find("b")` would result in `1`), or the methods `upper` or `lower` that can transform
a string to its uppercase/lowercase variants (e.g., `"aBc".upper()` would result in `"ABC"`).

In this exercise, you will receive a non-empty string `s` as input, which will always contain a colon (`:`).
Write a program that takes such a string and transforms all characters before the colon to lowercase and
all characters after the colon to uppercase. For example, the string `"aB:cD"` should be transformed into
`"ab:CD"` and stored in a variable called `res`. Of course, your program should work for arbitrary input strings.

Assume that the input variables are provided by the environment, you do not have to define them yourself. 
