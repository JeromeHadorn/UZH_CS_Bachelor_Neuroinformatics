# The following variables will be provided by the grading environment, you can
# access them without declaration. However, you can freely adopt the following
# values to play around with the script, as long as you keep them in the "if".
if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    d = 4


# a - (b^2 / (c - d * (a + b)))
# define the formula here
res = a - ((b ** 2) / (c - d * (a + b)))
print(res)
