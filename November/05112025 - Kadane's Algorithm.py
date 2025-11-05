# Kadane's algorithm

def solution1(arr):
    result = arr[0]
    maxi = float('-inf')
    for i in arr:
        maxi = max(maxi+i, i)
        result = max(result, maxi)

    return result

def solution2(arr):
    start = 0
    end = 0
    curr = 0
    maxi = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        if maxi + arr[i] < arr[i]:
            maxi = arr[i]
            curr = i
        else:
            maxi += arr[i]

        if maxi > result:
            result = maxi
            start = curr
            end = i

    return arr[start:end+1]
