# Search if subarray b is present in array a

def search1(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    temp = []
    for i in range(n-m+1):
        if arr1[i:i+m] == arr2:
            temp.append(i)
    return temp


arr1 = [2, 4, 1, 0, 4, 1, 1]
arr2 = [4,1]
print(search1(arr1,arr2))
print(search2(arr2,arr2))