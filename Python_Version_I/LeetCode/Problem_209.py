# Minimum sized subarray sum

def minimum(arr, target):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        if arr[0] >= target:
            return 1
        else:
            return 0
    if n == 2:
        if arr[0] >= target or arr[1] >= target:
            return 1
        elif arr[0] + arr[1] >= target:
            return 2
        else:
            return 0
    arrs = []
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(arr[i:j]) >= target:
                arrs.append(j-i)
    result = min(arrs)
    return result

# using sliding window
def minimum2(arr, target):
    n = len(arr)
    left = 0
    result = 0
    minimum = float('inf')
    for right in range(n):
        result += arr[right]
        while result >= target:
            minimum = min(minimum, right - left + 1)
            result -= arr[left]
            left += 1
    if minimum == float('inf'):
        return 0
    return minimum


target = 7
nums = [2,3,1,2,4,3]
print(minimum2(nums, target))