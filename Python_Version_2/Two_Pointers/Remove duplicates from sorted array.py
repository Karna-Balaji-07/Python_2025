# remove duplicates from sorted array

def solution1(arr):
    n = len(arr)
    index = 0
    for i in range(1, n):
        if arr[i] != arr[index]:
            index += 1
        arr[index] = arr[i]

    return arr