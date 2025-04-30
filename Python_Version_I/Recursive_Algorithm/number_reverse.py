# find the value of a number raised to ites reverse

def reverses(n):
    stack = []
    for char in n:
        if stack and stack[-1] == char:
            continue
        stack.append(char)
    return "".join(stack)
n = "geeksforgeeks"
print(reverses(n))