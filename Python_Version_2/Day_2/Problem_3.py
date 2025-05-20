# Apply Operations on Array

def solution1(arr):
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = arr[i] * 2
            arr[i+1] = 0
    result = []
    for i in arr:
        if i != 0:
            result.append(i)
    result.extend([0]*(len(arr)-len(result)))
    return result

arr = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
print(solution1(arr))