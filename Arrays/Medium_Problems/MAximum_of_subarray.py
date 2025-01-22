# K sized subarray maximum

def maximum(arr,k):
    n=len(arr)
    result=[]    
    for i in range(n):
        if i+k>n:
            break
        else:
            maxi = max(arr[i:i+k])
            result.append(maxi)
    return result

def maximum1(arr,k):
    n=len(arr)
    result=[]
    for i in range(n-k+1):
        result.append(max(arr[i:i+k]))
    return result

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print(maximum(arr,k))     
print(maximum1(arr,k))

