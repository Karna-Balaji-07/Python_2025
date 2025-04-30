# Merge two sorted arrays

def solution1(arr1,arr2):
    result = arr1+arr2
    result.sort
    return result

def solution2(arr1,arr2):
    j = 0
    for i in range(len(arr1)):
        if arr1[i] == 0:
            arr1[i] = arr2[j]
            j += 1
    arr1.sort()
    return arr1

def solution3(arr,arrs):
    left = 0
    right = 0
    n = len(arr)
    m = len(arrs)
    result = []
    while left < n and right < m:
        if arr[left] < arrs[right]:
            result.append(arr[left])
            left+= 1
        else:
            result.append(arrs[right])
            right += 1
    while left < n:
        result.append(arr[left])
        left += 1
    while right < m:
        result.append(arrs[right])
        right += 1
    return result


arr = [1,4,7,9]
arrs = [2,5,8]
print(solution3(arr,arrs))