# Maximum subarray sum - kadane's algorithm

def solution1(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sums = sum(arr[i:j+1])
            maxi = max(maxi,sums)
    return maxi

def solution2(arr):
    maxs = arr[0]
    sums = arr[0]
    for i in range(1,len(arr)):
        sums  = max(arr[i], arr[i]+sums)
        maxs = max(sums, maxs)
    return maxs

arr = [2, 3, -8, 7, -1, 2, 3]
print(solution1(arr))
print(solution2(arr))