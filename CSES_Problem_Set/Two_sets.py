#Two-Sets

def two_sets(n):
    arr = []
    for i in range(n):
        arr.append(i)
    for i in range(1,n):
        sum1 = sum(arr[:i])
        sum2 = sum(arr[i+1:])
        if sum1==sum2:
            return i
    return -1

n  = 7
result = two_sets(n)
if result==-1:
    print("NO")
else:
    print("YES")
    print(result)
    print()