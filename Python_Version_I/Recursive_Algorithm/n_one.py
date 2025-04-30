# print from n to 1

def prints(n):
    if n == 0:
        return
    print(n)
    prints(n-1)

n = 10
print(prints(n))