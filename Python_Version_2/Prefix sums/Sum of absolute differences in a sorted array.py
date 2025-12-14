# sum of absolute differences in sorted array

def solution(arr):
    prefix = [0] * len(arr)
    result = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    for i in range(len(arr)):
        result[i] = (arr[i]*(i+1) - prefix[i] + (prefix[len(arr)-1]-prefix[i]) - arr[i]* (len(arr)-i-1))
    return result