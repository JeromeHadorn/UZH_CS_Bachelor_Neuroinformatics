# Password Validation

A password should contain a variety of characters to make it harder
to guess. You are part of a team that develops a new application,
which requires passwords to satisfy the following rules. 

* Has a length of 8-16 chars
* Only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
* Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars

Implement a checker that decides whether a given password candidate
is valid. The password candidate will be given to you in a variable
`pwd`. Write a program that checks whether `pwd` satisfies all rules
and store the decision in a variable called `is_valid`.

While working on this task, three utilities will make your life easier: Use *isupper*/*islower* to decide whether a string is upper case or lower case (e.g., `"A".isupper()` is `True`) and *isdigit* to check if it is a number (e.g., `"3".isdigit()` is `True`). Remember that you can also use the `in` operator to check whether a specific character exists in a string (e.g., `"a" in "abc"` is `True`).

Assume that the input variable is provided by the environment, you do
not have to define it yourself. 
