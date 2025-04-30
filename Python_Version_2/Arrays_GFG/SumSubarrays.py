# Sum of all subarrays

def subarraysum(arr):
    sums = 0
    for i in range(len(arr)):
        temp = 0
        for j in range(i,len(arr)):
            temp += arr[j]
            sums += temp
    return sums

def sums1(arr):
    n = len(arr)
    sums = 0
    for i in range(len(arr)):
        sums += arr[i] * (n-i) * (i+1)
    return sums

arr = [1,2,3]
print(sums1(arr))