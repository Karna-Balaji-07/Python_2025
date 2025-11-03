# Maximum Subarray sum

def solution1(arr):
    maxi = 0
    for i in range(1,len(arr)):
        sums = 0
        for j in range(i+1,len(arr)):
            sums += arr[j]
        maxi = max(maxi,sums)
    return maxi

def solution2(arr):
    result = arr[0]
    maxi = arr[0]
    for i in range(1,len(arr)):
        maxi = max(maxi+arr[i], arr[i])
        result = max(result,maxi)
    return result


arr =  [2, 3, -8, 7, -1, 2, 3]
print(solution2(arr))
