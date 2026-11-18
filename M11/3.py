# MODULE 11: FUNCTIONS
# 3: Functional functions
# Diff: Easy

# What are functions for?
# Well, they're mostly used on things that are repetatative
# And to make things cleaner and organized

def line (length: int = 10):
    text = "".join(["-" for i in range(length)])
    print(text)

def c2f (c: str):
    return c * 9 / 5 + 32



line(40)
print("°Celcius to °Fahrenheit")
line(20)
print("From?: ", end = "")
fr = float(input())
print("To?: ", end = "")
to = float(input())
print("Step?: ", end = "")
by = float(input())
line()
print()

i = fr

while i <= to:
    print(f"{i} °C  =  {c2f(i):.2f} °F")
    i += by

line(40)