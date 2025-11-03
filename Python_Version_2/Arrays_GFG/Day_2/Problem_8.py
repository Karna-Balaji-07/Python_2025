# 75. sort colors
# Dutch National Flag problem
def solution1(arr):
    n = len(arr)
    low = 0
    high = n- 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1

    return arr

arr = [1,0,2,0,0,1,1,2]
print(solution1(arr))