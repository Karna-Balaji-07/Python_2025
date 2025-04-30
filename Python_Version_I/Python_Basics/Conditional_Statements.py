# conditional statement

# if condition
if 10 > 20:
    print(10)
print(20)

# if-else condition
if 10 > 20:
    print(10)
else:
    print(20)

# if..else chain statement
letter = "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B and C")


# if-elif statement example
letter = "A"

if letter == "B":
    print("letter is B")
elif letter == "C":
    print("letter is C")
elif letter == "A":
    print("letter is A")
else:
    print("letter isn't A, B or C")

# Ternary Operation
# Python program to demonstrate nested ternary operator
a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")