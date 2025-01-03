# Binary search algorithm

# Iterative Binary search algorithm

def binary1(arr, low, high, element):
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            high = mid - 1
        elif arr[mid] < element:
            low = mid + 1
    return -1

arr= [1,4,9,16,24,36,38,42,64]
low = 0
high = len(arr) -1
element = 16
print(binary1(arr,low,high,element))
element = 3
print(binary1(arr,low,high,element))


# Recursive Binary search algorithm

def binary2(arr,low, high,element):
    if low <= high:
        mid = (low + high ) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return binary2(arr,low, mid-1, element)
        elif arr[mid] < element:
            return binary2(arr,mid+1, high, element)
    return -1


arr= [1,4,9,16,24,36,38,42,64]
low = 0
high = len(arr) -1
element = 16
print(binary2(arr,low,high,element))
element = 3
print(binary2(arr,low,high,element))