# Count inversions in a matrix

def inversion(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j] and j > i:
                count += 1
    return count

arr = [2,4,1,3,5]
print(inversion(arr))