# Leaders in an array

def solution1(arr):
    result = [arr[-1]]
    n = len(arr)
    for i in range(n-2,-1,-1):
        if arr[i] > result[-1]:
            result.append(arr[i])
    return result[::-1]


arr = [10, 22, 12, 3, 0, 6]
