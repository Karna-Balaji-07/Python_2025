# Remove duplicates from sorted array


'''
The idea is to create a temporary array to store all the unique elements in the array and then be using arr[:] = arr to return the 
original array

'''
def duplcates(arr):
    arrs = []
    for i in arr:
        if i not in arrs:
            arrs.append(i)
    arr[:] = arrs
    return arr

def duplicates1(arr):
    n = len(arr)
    if not arr:
        return 0
    j = 0
    for i in range(n):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j+1
arr = [1,1,1,1,1,2,2,2,3,4,4,5]
print(duplicates1(arr))