# search in rotated sorted array

def solution1(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low +high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] >= arr[low]:
            if target >= arr[low ] and target < arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if target > arr[mid] and target <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1

