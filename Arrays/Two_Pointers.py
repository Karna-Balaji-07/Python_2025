# Two_Pointer technique

def two_sum(arr, target):
    n = len(arr)
    left = 0
    right = n-1
    arr.sort()
    while left < right:
        sums = arr[left] + arr[right]
        if sums == target:
            return True
        elif sums < target:
            left += 1
        elif sums > target:
            right -= 1
    return False

arr = [10, 20, 35, 50]
target = 70
print(two_sum(arr,target))