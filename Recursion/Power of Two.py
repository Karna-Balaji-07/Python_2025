# Power of two

def soln1(n):
    while n % 2 == 0:
        n //= 2
    return n == 1

def soln2(n):
    return n > 0 and (n & (n-1)) == 0

def func(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    return n % 2 == 0 and func(n//2)

n = 16
print(soln1(n))