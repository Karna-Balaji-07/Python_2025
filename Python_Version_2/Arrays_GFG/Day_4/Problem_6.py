# sort an array in wave form

def solution1(arr):
    n =  len(arr)
    for i in range(1, n,2):
        if i > 0 and arr[i] > arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
        if i < n-1 and arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        
    return arr

arr = [1,2,3,4,5]
print(solution1(arr))