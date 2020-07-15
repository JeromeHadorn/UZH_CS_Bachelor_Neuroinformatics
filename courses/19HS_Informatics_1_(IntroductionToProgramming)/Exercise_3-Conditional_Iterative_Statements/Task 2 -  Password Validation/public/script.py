# The following variable will be provided by the grading environment, you can
# access it without declaration. However, you can freely adopt the following
# value to play around with the script, as long as you keep it in the "if".
if __name__ == "__main__":
    pwd = "aaBB**11#"

# check whether `pwd` is a valid password

character_counter = 0
# Has a length of 8-16 chars
# Only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
# Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars
lowercase_counter = 0
uppercase_counter = 0
digit_counter = 0
special_counter = 0
unrecognizedCharacterFlag = False


for character in pwd:

    character_counter = character_counter + 1
    print(character)
    if character.isupper():
        uppercase_counter = uppercase_counter + 1
    elif character.islower():
        lowercase_counter = lowercase_counter + 1
    elif character.isdigit():
        digit_counter = digit_counter + 1
    elif character == "+" or character == "-" or character == "*" or character == "/":
        special_counter = special_counter + 1
    else:
        unrecognizedCharacterFlag = True
        print("not a valid character")




if lowercase_counter >= 2 and uppercase_counter >= 2 and digit_counter >= 2 and special_counter >= 2 and 8 <= character_counter <= 16 and unrecognizedCharacterFlag == False:
    is_valid = True
else:
    is_valid = False

print(pwd)
print(character_counter,lowercase_counter,uppercase_counter,digit_counter,special_counter,unrecognizedCharacterFlag)

print(is_valid)