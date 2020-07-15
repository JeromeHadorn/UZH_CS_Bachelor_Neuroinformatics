# The following variables will be provided by the grading environment, you can
# access them without declaration. However, you can freely adopt the following
# value to play around with the script, as long as you keep it in the "if".
if __name__ == "__main__":
    s = "aaaaaB:cd"

# perform the transformation

indexOfColon = s.find(":")

firstPart = s[:indexOfColon]
secondPart = s[indexOfColon:]
res = firstPart.lower() + secondPart.upper()
print(res)
