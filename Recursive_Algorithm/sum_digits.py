# sum of digits using recursion

def recursion1(n):
    if n == 0:
        return 0
    return n % 10 + int(recursion1(n//10))

print(recursion1(12345))