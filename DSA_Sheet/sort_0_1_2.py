# Sort an array of 0s, 1s and 2s 

# Using inbuilt sorting function
def sorts1(arr):
    arr.sort()
    return arr

# By counting the number of 0,1 and 2
def sorts2(arr):
    zero = 0
    ones = 0
    twos = 0
    for i in arr:
        if i == 1:
            ones += 1
        elif i == 2:
            twos += 1
        else:
            zero += 1
    index = 0
    for i in range(zero):
        arr[index] = 0
        index += 1
    for i in range(ones):
        arr[index] = 1
        index+= 1
    for i in range(twos):
        arr[index] = 2
        index += 1
    return arr

# Dutch National Flag aglgorithm
def sorts3(arr):
    n = len(arr)
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1

    return arr


arr = [1,1,0,0,2,0,1]
print(sorts2(arr))

    
        

