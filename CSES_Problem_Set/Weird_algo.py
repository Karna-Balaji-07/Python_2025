#  Weird algo

def weird(n):
    arr = []
    arr.append(n)
    while n != 1:
        if n%2==0:
            n= n  // 2
        else:
            n = n*3 + 1
        arr.append(n)
    return arr

n = int(input())
result = weird(n)
print(" ".join(map(str,result)))