# Move all zeros to the end of the array

def solution1(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[right] == 0:
            right -= 1
        elif arr[left] != 0:
            left += 1
    print(arr)

def solution2(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j],arr[i] = arr[i],arr[j]
            j += 1

    print(arr)

arr = [2,0,1,4,5,0,0,1,3,5,0,2,0,5]
solution1(arr)
solution2(arr)