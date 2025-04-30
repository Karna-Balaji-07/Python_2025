# Maximum subarray sum

def subarray(arr):
    n=len(arr)
    maximum = arr[0]
    sums = arr[0]
    for i in range(1,n):
        sums = max(arr[i],sums+arr[i])
        maximum = max(maximum,sums)
    return maximum

def subarray1(arr):
    n=len(arr)
    sums=0
    maximum = -9999999999999
    for i in arr:
        sums+=i
        if sums > maximum: maximum=sums
        if sums < 0 : sums=0
    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(subarray(nums))
print(subarray1(nums))