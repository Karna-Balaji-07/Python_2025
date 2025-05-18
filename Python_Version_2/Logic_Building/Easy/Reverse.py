# reverse an  integer

def solution1(n):
    rev = 0
    num = n
    while num > 0:
        temp = num % 10
        rev = 10*rev + temp
        num //= 10
    return rev

n = 12345
print(solution1(n))