# The following variable will be provided by the grading environment, you can
# access it without declaration. However, you can freely adopt the following
# value to play around with the script, as long as you keep it in the "if".
if __name__ == "__main__":
    circumference = 90.01

# determine the right size of a shirt
size = ""

if 80 <= circumference <= 90:
    size = "XS"
elif 90 < circumference <= 98:
    size = "S"
elif 98 < circumference <= 104:
    size = "M"
elif 104 < circumference <= 111:
    size = "L"
elif 111 < circumference <= 124:
    size = "XL"
else:
    size = "N/A"


print(circumference,size)