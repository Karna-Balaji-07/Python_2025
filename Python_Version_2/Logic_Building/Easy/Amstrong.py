# Armstrong Numbers

def solution1(n):
    s = len(str(n))
    num = n
    sums = 0
    while num > 0:
        temp = num % 10
        sums += temp ** s
        num //= 10

    return sums == n

n = 153
print(solution1(n))