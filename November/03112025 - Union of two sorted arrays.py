# Union of two sorted arrays

def solution1(arr1,arr2):
    arr = arr1 + arr2
    arr = list(set(arr))
    return arr

def solution2(arr1, arr2):
    left = 0
    right = 0
    n = len(arr1)
    m = len(arr2)
    arr = []
    while left < n and right < m:
        if arr1[left] < arr2[right]:
            if arr[-1] != arr1[left] or len(arr) == 0:
                arr.append(arr1[left])
            left += 1
        else:
            if arr[-1] != arr2[right] or len(arr) == 0:
                arr.append(arr2[right])
            right += 1

    while left < n:
        if arr[-1] != arr1[left]:
            arr.append(arr1[left])
        left += 1

    while right < m:
        if arr[-1] != arr2[right]:
            arr.append(arr2[right])
        right += 1

    return arr

