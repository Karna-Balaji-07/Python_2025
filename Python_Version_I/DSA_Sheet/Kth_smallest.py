# K'th smallest element in unsorted array

# naive approach
def smallest1(arr,k):
    arr.sort()
    return arr[k-1]

# using counting sort algorithm
def smallest2(arr,k):
    dicts = {}
    n = len(arr)
    maxi = max(arr)
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    count = 0
    for i in range(maxi):
        if i in dicts:
            count += dicts[i]
            if count >= k:
                return i
    return -1

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(smallest2(arr,k))