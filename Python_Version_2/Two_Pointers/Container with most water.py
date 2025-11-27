# Return the continer with most water

def solution1(arr):
    left = 0
    n = len(arr)
    right = n-1
    result = 0
    while left < right:
        water = min(arr[left, arr[right]]) * (right-left)
        result = max(result, water)
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1

    return result