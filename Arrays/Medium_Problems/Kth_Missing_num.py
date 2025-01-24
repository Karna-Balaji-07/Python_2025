# Kth missing positive number in a sorted array

def missing(arr,k):
    n = len(arr)
    for i in range(n):
        if arr[i] > k+i:
            return k+i

arr =  [2, 3, 4, 7, 11]
print(missing(arr,5))