# Union of two sorted arrays with duplicates

def union(arr1,arr2):
    arr = []
    for i in arr1:
        if i not in arr:
            arr.append(i)
    for i in arr2:
        if i not in arr:
            arr.append(i)
    arr.sort()
    return arr

def union2(arr1,arr2):
    arr = arr1+arr2
    arrs = sorted(set(arr))
    return arrs

def unions(arr1,arr2):
    result = []
    i,j=0,0
    while i<len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or arr1[i] !=result[-1]:
                result.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            if not result or arr2[j] != result[-1]:
                result.append(arr2[i])
            j+=1
        else:
            if not result or arr1[i] != result[-1]:
                result.append(arr1[i])
            i+=1
            j+=1
    while i < len(arr1) :
        if not result or arr1[i] != result[-1]:
            result.append(arr1[i])
        i+=1
    while j < len(arr2):
        if not result or arr2[j] != result[-1]:
            result.append(arr2[j])
        j+=1
    return result 
    
        

a= [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
print(union(a,b))
print(union2(a,b))
print(unions(a,b))