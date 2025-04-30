# Square root of a number
import math as math
def solution1(n):
    return int(math.sqrt(n))

def solution2(n):
    first = 0
    last = n
    result = 0
    while first <= last:
        mid = last+first //2
        if mid * mid == n:
            return mid
        if mid * mid < n:
            result = mid
            first += 1
        else:
            last -= 1
    return result

n= 10
print(solution2(n))