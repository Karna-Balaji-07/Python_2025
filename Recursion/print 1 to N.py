# Print 1 to n using recursion

def func(i,n):
    if i > n:
        return
    print(i,end=" ")
    func(i+1,n)

def func1(n):
    if n == 0:
        return
    func1(n-1)
    print(n)


func(1,10)