# Move all the zeros to the end

def move1(arr):
    n = len(arr)
    index = 0
    for i in arr:
        if i != 0:
            arr[index] = i
            index += 1
    while index < n:
        arr[index] = 0
        index += 1
    return arr

def move2(arr):
    index = 0
    n = len(arr)
    for i in range(n):
        if arr[index] != 0:
            arr[index],arr[i] = arr[i],arr[index]
            index += 1
    return arr

arr = [0,1,0,3,12]
print(move1(arr))
print(move2(arr))