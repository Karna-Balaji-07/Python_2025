# 3sum problem with unique triplets

def solution1(arr,target):
    n = len(arr)
    arr.sort()
    result = []
    for first in range(n-2):
        if first > 0 and arr[first] == arr[first-1]:
            continue
        second = first + 1
        third = n-1
        while second < third:
            curr = arr[first] + arr[second] + arr[third]
            if curr == target:
                result.append([first, second,third])
                second += 1
                third -= 1
                while second < third and arr[second] == arr[second - 1]:
                    second += 1
                while second < third and arr[third] == arr[third+1]:
                    third -= 1

            elif curr > target:
                third   -= 1
            else:
                second += 1

    return result