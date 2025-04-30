# Even greater than odd
# arr[i] >= arr[i-1], if i is even.
# arr[i] <= arr[i-1], if i is odd.


def evens1(arr):
    n = len(arr)
    index = 1
    for i in range(0,n):
        if i % 2 == 0:
            if arr[i] >= arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
        elif i % 2 != 0:
            if arr[i] <= arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
    
    for i in range(1, len(arr)):
        if i % 2 != 0:
            if (arr[i] < arr[i-1]):
                return False
        else:
            if (arr[i] > arr[i-1]):
                return False
    return True

arr = [1,2,3,4,5]
print(evens1(arr))

