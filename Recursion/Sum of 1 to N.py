# sum of first 1 to N numbers

def func(n,sum):
    if n < 0:
        print(sum)
        return
    func(n-1, sum+n)

def func1(n):
    if n == 0:
        return 0
    return n + func1(n-1)

print(func1(10))



