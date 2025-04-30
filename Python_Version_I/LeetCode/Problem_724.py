# Pivot index

def pivot_Index(arr):
    n=len(arr)
    i=0
    while i < n-1:
        sum1 = sum(arr[:i])
        sum2=sum(arr[i+1:])
        if sum1==sum2:
            return i
        i+=1
    return -1

def pivot_Index1(arr):                                                      
    leftSum=0
    rightSum = sum(arr)
    for index,element in enumerate(arr):
        rightSum -= element
        if rightSum == leftSum:
            return index
        leftSum += element
    return -1

nums = nums = [-1,-1,0,1,1,0]
print(pivot_Index1(nums))