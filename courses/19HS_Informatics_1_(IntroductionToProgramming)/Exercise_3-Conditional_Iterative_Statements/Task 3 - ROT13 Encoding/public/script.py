# The following variable will be provided by the grading environment, you can
# access it without declaration. However, you can freely adopt the following
# value to play around with the script, as long as you keep it in the "if".
if __name__ == "__main__":
    plain_text = "a#bc"
    shift_by = -1

encoded = ""
remainder = shift_by % 26


if shift_by < 0:
    remainder = 26 - remainder


lowercase_range = range(97,123,122)
uppercase_range = range(65,91,90)

# perform a ROTn encoding
for character in plain_text:
    if character.isalpha():
        ascii = ord(character)
        if character.isupper():
            index = ((ascii - 65) + shift_by) % 26
            encoded = encoded + chr(65 + index)
        elif character.islower():
            index = ((ascii - 97) + shift_by) % 26
            
            encoded = encoded + chr(97 + index)
    else:
        encoded = encoded + character
        continue
        






print(encoded)