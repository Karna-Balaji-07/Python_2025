# Peak element 

def peak(arr):
    n = len(arr)
    first = -1
    last = -1
    for i in range(n):
        if i <= 0 and n <= 1:
            return i
        if i == 0  and arr[i] > arr[i+1] and arr[i] > first:
            return i
        elif i+1 < n and arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            return i
        elif i == n-1 and arr[i] > last and arr[i] > arr[i-1]:
            return i
        
    return i

def peak1(arr):
    n = len(arr)
    for i in range(n):
        left = True
        right = True
        if i > 0 and arr[i] <= arr[i-1]:
            left = False
        if i < n-1 and arr[i] <= arr[i+1]:
            right = False
        if left and right:
            return i


arr = [-1]
print(peak(arr))
print(peak1(arr))
            
