# Print n to 1

def func(n):
    if n < 1:
        return
    print(n,end=" ")
    func(n-1)

def func1(i,n):
    if i > n:
        return
    func1(i+1,n)
    print(i,end=" ")

func1(1,10)