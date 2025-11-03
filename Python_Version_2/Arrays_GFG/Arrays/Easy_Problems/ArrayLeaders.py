# Leaders in an array

def solution1(arr):
    result = []
    maxi = arr[-1]
    result.append(maxi)

    n = len(arr)
    for i in range(n-2,-1,-1):
        if arr[i] >= maxi:
            maxi = arr[i]
            result.append(maxi)
        
    return result[::-1]

arr = [16, 17, 4, 3, 5, 2]
