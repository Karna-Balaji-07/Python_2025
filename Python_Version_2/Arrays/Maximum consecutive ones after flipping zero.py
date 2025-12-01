# Find the maximum consecutive ones after flipping zero

def solution1(arr,k):
    count = 0
    left = 0
    right = 0
    result = 0
    while right < len(arr):
        if arr[right] == 0:
            count += 1
        while count > k:
            if arr[left] == 0:
                count -= 1
            left += 1

        result = max(result, right-left+1)
        right += 1
    return result

arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]; k = 2
print(solution1(arr,k))