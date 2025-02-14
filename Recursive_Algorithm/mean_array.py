# Mean of an array using recursion

def recursion(arr,n):
    if n == 1:
        return arr[n-1]
    else:
        return ((recursion(arr,n-1) * (n-1)+ arr[n-1])/n)
    
def recursion1(arr,n):
    if n == 1:
        return arr[n-1]
    else:
        return arr[n-1]+recursion1(arr,n-1)
    
def mean(arr,n):
    if n == 1:
        return arr[n-1]
    else:
        return recursion1(arr,n)/n

arr = [1,2,3,4,5]
print(recursion(arr,len(arr)))
print(mean(arr,len(arr)))