# Find the GCD of two numbers

def solution1(n1,n2):
    for i in range(1, min(n1,n2)+1):
        if n1 % i == 0  and n2 % i == 0:
            gcd = i

    return gcd

def solution2(n1,n2):
    for i in range(min(n1,n2), 0,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    

def solution3(n1,n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1  = n1 % n2
        else:
            n2 = n2 % n1

    if n1 == 0:
        return n2
    return n1

n1 = 20
n2 =  15
print(solution1(n1,n2))
print(solution2(n1,n2))
print(solution3(n1,n2))