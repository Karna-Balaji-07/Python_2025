# Move Move all negative numbers to beginning and positive to end with constant extra space

# Using sort function
def move1(arr):
    arr.sort()
    return arr

# Using 2 temporary arrays that store negative and positive numbers
def move2(arr):
    positive = []
    negative = []
    for i in arr:
        if i > 0:
            positive.append(i)
        else:
            negative.append(i)
    result = negative+positive
    return result

# Swapping the element using temporary variable
def move3(arr):
    j = 0
    n = len(arr)
    for i in range(n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    return arr

# Using two pointers that point to the right and left side of the arrray
def move4(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        elif arr[right] > 0 and arr[left] > 0:
            right -= 1
        else:
            left+=1
            right -= 1
    return arr

# Using the dutch national flag algorithm
def move5(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        if arr[low] < 0:
            low += 1
        elif arr[high] > 0:
            high -= 1
        else:
            arr[low],arr[high] = arr[high],arr[low]
    return arr

def move6(arr):
    i = 0
    n = len(arr)
    for j in range(n):
        if arr[j] > 0:
            arr[i] = arr[j]
            i += 1
    for j in range(n):
        if arr[j] < 0:
            arr[i] = arr[j]
            i += 1
    return arr

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(move6(arr))