# Minimum swaps required to group all the ones together

def solution1(arr):
    ones = arr.count(1)
    arr = arr + arr  # <-- this is why answer becomes 3

    count = 0
    i = 0
    swaps = 0

    while i < len(arr) and count < ones:
        if arr[i] == 0:
            swaps += 1
        count += 1
        i += 1

    min_swaps = swaps

    left = 0
    while i < len(arr):
        if arr[left] == 0:
            swaps -= 1
        if arr[i] == 0:
            swaps += 1

        min_swaps = min(min_swaps, swaps)

        left += 1
        i += 1

    return min_swaps


arr = [0 ,1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1 ,1 ,0 ,1, 0, 1]
print(solution1(arr))