# SEarch in 2D matrix

def solution1(arr, target):
    for arrs in arr:
        for i in arrs:
            if i == target:
                return True

    return False


def solution2(arr, target):
    def binary(arr, target):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid+1
            else:
                high = mid - 1
        return -1
    for i in range(len(arr)):
        if arr[i][0] < target <= arr[i][len(arr[0])-1]:
            return binary(arr[i], target)

    return False

def solution3(arr, target):
    low = 0
    high = len(arr) * len(arr[0]) - 1
    while low <= high:
        mid = (low+high) // 2
        row = mid // len(arr[0])
        col = mid % len(arr[0])
        if arr[row][col] == target:
            return True
        elif arr[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False    