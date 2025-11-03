# Maximum consecutive ones

def solution1(arr):
    n = len(arr)
    count = 0
    result = 0
    for i in arr:
        if i == 1:
            count += 1
        else:
            result = max(result, count)
            count = 0
        result = max(result, count)
    return result

def solution2(arr):
    left = 0
    result = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            left = right +1

        else:
            result = max(result, right-left+1)

    return result

arr = [1,1,0,0,1,1,1]
print(solution1(arr))
