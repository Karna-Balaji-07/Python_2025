# Find the maximum product of a triplet subsequence in an array

def solution(arr):
    arr.sort()
    return max(arr[0]*arr[1]*arr[-1],arr[-1]*arr[-2]*arr[-3])

def solution2(arr):
    maxA = float('-inf')
    maxB = float('-inf')
    maxC = float('-inf')
    minA = float('inf')
    minB = float('inf')

    for i in range(len(arr)):
        if arr[i] > maxA:
            maxC = maxB
            maxB= maxA
            maxA = arr[i]
        elif arr[i] > maxB and arr[i] < maxA:
            maxC = maxB
            maxB = arr[i]
        elif arr[i] > maxC and arr[i]< maxB:
            maxC = arr[i]

        if arr[i] < minA:
            minB = minA
            minA = arr[i]
        elif arr[i] < minB and arr[i] > minA:
            minB = arr[i]


    prod1 = maxB*maxC*maxA
    prod2 = maxA*minA*minB
    return max(prod1, prod2)

arr = [-10, -3, -5, -6, -20]
print(solution2(arr))