# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def fac(n):
    if n == 0:
        return 1
    else:
        return fac(n-1) * n


# You can play around with your solution from within this block.
if __name__ == '__main__':
    print("fac({}) = {}".format(8, fac(8)))
