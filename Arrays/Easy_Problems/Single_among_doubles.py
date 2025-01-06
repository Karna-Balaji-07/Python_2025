# Single among Doubles

def singles(arr):
    n = len(arr)
    temp =[]
    i = 0
    while i < n:
        if i+1 < n and arr[i] == arr[i+1]:
            i += 2
        else:
            temp.append(arr[i])
            i += 1 
    return temp[0]

def singles2(arr):
    n = len(arr)
    for i in range(0,n-1,2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return arr[n-1]

arr = [1,1,2,3,3]
print(singles(arr))
print(singles2(arr))
