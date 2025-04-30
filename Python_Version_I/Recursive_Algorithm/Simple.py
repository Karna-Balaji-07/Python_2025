# sum of n natural numbers

def sum1(n):
    if n == 1:
        return 1
    return n + sum1(n-1)

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

n = 10
print(sum1(n))
print(factorial(5))



