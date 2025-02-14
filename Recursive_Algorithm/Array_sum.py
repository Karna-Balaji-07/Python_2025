# sum of elements in array

def recursion1(arr,n):
    if n == 1:
        return arr[n-1]
    return arr[n-1] + recursion1(arr,n-1)

arr = [2,4,6,8]
n = len(arr)
print(recursion1(arr,n))

