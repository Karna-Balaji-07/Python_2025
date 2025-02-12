# Maximum subarray sum - kadane's algorithm

def solution1(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sums = sum(arr[i:j+1])
            maxi = max(maxi,sums)
    return maxi

arr = [2, 3, -8, 7, -1, 2, 3]
print(solution1(arr))