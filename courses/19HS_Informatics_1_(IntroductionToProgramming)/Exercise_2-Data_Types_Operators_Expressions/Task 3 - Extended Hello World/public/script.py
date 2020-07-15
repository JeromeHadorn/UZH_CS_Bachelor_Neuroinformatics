# The following variables will be provided by the grading environment, you can
# access them without declaration. However, you can freely adopt the following
# values to play around with the script, as long as you keep them in the "if".
if __name__ == "__main__":
    name = "Hans"
    age = 37

# generate the greeting sentence
# "Hello Hans, you are 37 years old!"
greeting = "Hello " + name +", you are " + str(age) + " years old!"
print(greeting)

if "Hello Hans, you are 37 years old!" == greeting:
    print("it's true")
else:
    print("not true man")
