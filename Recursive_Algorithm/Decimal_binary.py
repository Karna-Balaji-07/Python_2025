# Decimal to bbinary conversion

def recursion1(n):
    if n == 0:
        return 0
    return n % 2 + 10 * int(recursion1(n//2))

def recursion2(n):
    if n == 0:
        return 0
    smallest = recursion2(n//2)
    return n % 2 + 10*smallest

n =4
print(recursion1(n))
print(recursion2(n))