# remove all the duplicates from the given array

def removeduplicates1(arr):
    arrs = []
    for i in arr:
        if i not in arrs:
            arrs.append(i)
    return arrs

def removeduplicates2(arr):
    arr.sort()
    index = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[index]:
            index  += 1
            arr[index] = arr[i]
    return arr[:index+1]


arr = [2,2,3,3,5,5,5,7]
print(removeduplicates2(arr))