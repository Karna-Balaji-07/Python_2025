# Two sum in sorted arrays

def two_sum(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        sums = arr[left]+arr[right]
        if sums == target:
            return [arr[left],arr[right]]
        elif sums > target:
            right -= 1
        else:
            left += 1
    return -1

arr = [-8,1,4,6,10,45]
print(two_sum(arr,16))
