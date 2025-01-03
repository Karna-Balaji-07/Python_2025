# Largest element in the array

def largest1(arr):
    n = len(arr)
    maxx = arr[0]
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j] > maxx:
                maxx = arr[j]
    return maxx

def largest2(arr):
    maxx = max(arr)
    return maxx

def largest3(arr):
    n = len(arr)
    maxs = arr[0]
    for i in range(1,n):
        if arr[i] > maxs:
            maxs = arr[i]
    return maxs

arr = [10,30,50,12,841,32,15,2410,74]
print(largest1(arr))
print(largest2(arr))
print(largest3(arr))