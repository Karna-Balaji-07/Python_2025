# 3sum closest to target

def solution1(arr, target):
    arr.sort()
    n = len(arr)
    mindiff = 0
    result = 0
    for first in range(n-2):
        second = first  + 1
        third = n-1
        while second < third:
            curr = arr[first] +  arr[second] + arr[third]
            diff = abs(target-curr)
            if diff < mindiff:
                mindiff = diff
                result = curr
            elif diff == mindiff:
                result = max(result, curr)
            if curr > target:
                third  -= 1
            else:
                second += 1
    return result
