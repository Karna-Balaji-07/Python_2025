# Remove duplicates in sorted array

def solution1(arr):
    k = 0
    for i in range(len(arr)):
        if i > 0 and arr[i] != arr[i-1]:
            arr[k] = arr[i-1]
            k += 1

    print(arr[:k])

arr = [1,1,1,2,2,3,3,3,3,4,4]
solution1(arr)