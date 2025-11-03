# 27. Remove element

def solution1(arr,value):
    index = 0
    i = 0
    while i < len(arr):
        if arr[i] == value:
            i += 1
        else:
            arr[index] = arr[i]
            index += 1
            i += 1
        
    return arr

arr = [3,2,2,3]
print(solution1(arr,3))