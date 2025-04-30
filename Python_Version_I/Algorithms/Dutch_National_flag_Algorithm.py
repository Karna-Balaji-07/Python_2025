# Dutch national flag problem for sorting zeros, ones and twos

def dnfp(arr):
    n = len(arr)
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if arr[mid] == 1:
            mid += 1
        elif arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1
    return arr

arr = [0,1,0,2,2,0,1]
print(dnfp(arr))