# Minimum element in sorted and rotated array

def solution1(arr):
    return min(arr)

def solution2(arr):
    low = 0
    high = len(arr)-1
    while low < high:
        if arr[low] < arr[high]:
            return arr[low]
        mid = (high+low)//2
        if arr[mid] >arr[high]:
            low = mid+1
        else:
            high = mid
    return arr[low]


def solution3(arr):
    index = 0
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            index = i
    result = []
    result = arr[index:] + arr[:index]
    return result[0]

arr = [5,6,1,2,3,4]
print(solution2(arr))