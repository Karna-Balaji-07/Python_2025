# Minimize the maximum difference between the heights

def minimizer(arr,k):
    n=len(arr)
    arr.sort()
    res = arr[n-1] - arr[0]
    for i in range(1,n-1):
        if arr[i]-k < 0:
            continue
        minH = min(arr[0]+k,arr[i]-k)
        maxH = max(arr[i-1]+k,arr[n-1]-k)
        res = min(res, maxH-minH)
    return res

arr = [12, 6, 4, 15, 17, 10]
k=6
print(minimizer(arr,k))