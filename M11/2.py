# MODULE 11: FUNCTIONS
# 2: Defining a function
# Diff: Easy

# Ok, last example was useless
# Let's actually do something this time

# ----- Make em

# This
def printsSomething ():
    print("something")

# This
def returnsSomethin ():
    return "somethin"

# This
def takesSomething (something):
    print(f"took: {something}")

# This
def takesAndReturnsSomething (something):
    return f"took: {something}"


# ----- Call em

printsSomething()

gotSomething = returnsSomethin()
print(gotSomething)

takesSomething("SOMETHING")

gotTookSomething = takesAndReturnsSomething("someThing")
print(gotTookSomething)


# By default a function returns `None`
print(printsSomething())