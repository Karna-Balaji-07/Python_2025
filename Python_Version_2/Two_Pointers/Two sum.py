# Two sum in sorted and unsorted array

def solution1(arr,target):
    arr = sorted(arr)
    n = len(arr)
    left = 0
    right = n-1
    while left <= right:
        if arr[left] + arr[right] == target:
            return left,right
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1
    return -1

def solution2(arr,target):
    n = len(arr)
    s = set()
    for i in arr:
        diff = target - i
        if diff in set:
            return True
        s.add(i)

    return False

def solution3(arr,target):
    n = len(arr)
    dicts = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in dicts:
            return [i, dicts[diff]]
        dicts[arr[i]] = i

    return -1