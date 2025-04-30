# Count the  number of digits in n

def solution1(n):
    countt = 0
    while n > 0:
        countt += 1
        n //= 10
    return countt

def solution2(n):
    s = str(n)
    return len(s)

import math as m
def solution3(n):
    count = int(m.log10(n)+1)
    return count

n = 23432
print(solution3(n))