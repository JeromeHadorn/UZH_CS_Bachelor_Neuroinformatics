# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def is_prime(n):
    if n == 1:
        return "1 is the multiplicative identity"
    else:
        for x in range(2,1000000):
            if n % x == 0 and n != x:
                return "%d is not a prime number (%d * %d = %d)" % (n,x,n/x,n)
                break
        return "%d is prime" % (n)
    # implement this function
    pass


# You can play around with your solution from within this block.
if __name__ == '__main__':
    print(is_prime(125243))
