# Sort an array where a subarray of a sorted array is in reverse order

def sorts1(arr):
    arr.sort()
    return arr

def sorts2(arr):
    n = len(arr)
    start = -1
    end = -1
    for i in range(1,n):
         if arr[i] < arr[i-1]:
             start = i-1
             break
    i = n-2
    while i >= 0:
        if arr[i] > arr[i+1]:
            end = i+1
            break
        i -= 1
    
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    for i in range(n):
        print(arr[i],end=" ")

arr = [1, 7, 6, 5, 4, 3, 2, 8]
print(sorts1(arr))
sorts2(arr)