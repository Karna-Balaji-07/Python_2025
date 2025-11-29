# Minimize the maximum difference between the heights

def solution1(arr,k):
    arr.sort()
    n = len(arr)
    result = arr[n-1] - arr[0]
    for i in range(1,n):
        if arr[i] - k < 0:
            continue
        minH = min(arr[0]+k,arr[i]-k)
        maxH = max(arr[i-1]+k, arr[n-1]-k)
        result = min(result, maxH-minH)
    return result

k = 3; arr = [3, 9, 12, 16, 20]
arr = [1,5,8,10]
print(solution1(arr,k=2))
