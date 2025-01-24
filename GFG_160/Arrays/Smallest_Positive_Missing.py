# Smallest Positive number missing

def smallest(arr):
    arr.sort()
    res = []
    for i in arr:
        if i not in res and i > 0:
            res.append(i)
    for i in range(1,len(res)):
        if i != arr[i-1]:
            return i
    
        
arr = [2, -3, 4, 1, 1, 7]
print(smallest(arr))
