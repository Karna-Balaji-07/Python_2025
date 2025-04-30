# Left rotation by d times

# Method - 1 == Naive approach
def rotate1(arr,d):
    n = len(arr)
    d %= n # case when d > n
    for i in range(d):
        first = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first
    return arr

arr = [1,2,3,4,5,6]
d = 2
print(rotate1(arr,d))

# Method - 2 == Using Temporary Array
def rotate2(arr,d):
    n = len(arr)
    temp = []
    for i in range(d,n):
        temp.append(arr[i])
    for i in range(d):
        temp.append(arr[i])
    return temp

arr = [1,2,3,4,5,6]
d = 2
print(rotate2(arr,d))

#======================================================================================================#

# RIGHT ROTATION

# using temporary array     
def rotate3(arr,d):
    n = len(arr)
    temp = []
    for i in range(n-d,n):
        temp.append(arr[i])
    for i in range(n-d):
        temp.append(arr[i])
    return temp
arr = [1,2,3,4,5,6]
d = 2
print(rotate3(arr,d))
    