# Equilibrium Point

def point1(arr):
    n = len(arr)
    for i in range(1,n):
        sum1 = sum(arr[:i])
        sum2 = sum(arr[i+1:])
        if sum1==sum2:
            return i
    return -1

def point2(arr):
    n=len(arr)
    sum=0
    for i in arr:
        sum+=i
    right=sum
    left=0
    for i in range(n):
        right -= arr[i]
        if left==right:
            return i
        else:
            left+=arr[i]
    return -1 
    

arr = [-7, 1, 5, 2, -4, 3, 0]
print(point1(arr))
print(point2(arr))
