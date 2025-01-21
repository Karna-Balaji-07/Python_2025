# Move all zeroes to End

def move(arr):
    n= len(arr)
    index=0
    arrs =[0]*n
    for i in arr:
        if i != 0:
            arrs[index] = i
            index += 1
    return arrs

def move1(arr):
    n  = len(arr)
    index=0
    for i in arr:
        if i!=0:
            arr[index] = i
            index +=1
    while index < n:
        arr[index] = 0
        index+=1
    return arr

arr = [3,5,0,0,0,4]
print(move(arr))
print(move1(arr))