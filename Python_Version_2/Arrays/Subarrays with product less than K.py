# Number of subarrays having products less than K

def solution1(arr,k):
    if k <= 1:
        return 0

    product = 1
    count = 0
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= k and left <= right:
            product //= arr[left]
            left += 1
        count += (right - left + 1)
    return count
