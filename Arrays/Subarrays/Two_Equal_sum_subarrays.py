# Split an array into two equal Sum subarrays

def subarray1(arr,n):
    leftsum = 0
    for i in range(n):
        leftsum += arr[i]
        rightsum = 0
        for j in range(i+1,n):
            rightsum += arr[j]
        if leftsum == rightsum:
            return i+1
    return -1

def subarray2(arr,n):
    left = 0
    for i in range(n):
        left += arr[i]
    right = 0
    for i in range(n-1,-1,-1):
        right += arr[i]
        left -= arr[i]
        if right == left :
            return True
    return False

def split(arr,n):
    sub = subarray1(arr,n)
    if sub ==0 or sub == -1:
        return None
    for i in range(n):
        if sub == i:
            print("")
        print(arr[i],end=" ")

arr = [1,2,3,4,5,5]
n = len(arr)
split(arr,n)
