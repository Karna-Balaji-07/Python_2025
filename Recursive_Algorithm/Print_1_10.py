# Print one to ten using recursion

def recursion(n):
    if n > 0:
        recursion(n-1)
        print(n,end=" ")

def recursion1(n):
    if n > 0:
        print(n,end=" ")
        recursion1(n-1)
print(recursion1(10))

