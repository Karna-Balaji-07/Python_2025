# Print 1 to n without loops

def prints(n):
    if n > 0:
        prints(n-1)
        print(n,end=" ")

n = 10
print(prints(n))

