# Kth Smallest  Element

def smallest1(arr, k):
    n = len(arr)
    arrs = list(set(arr))
    return arrs[k-1]

def smallest2(arr,k):
    n = len(arr)
    arrs = []
    i=0
    while i < k:
        mins = min(arr)
        arrs.append(mins)
        arr.remove(mins)
        i+=1
    return arrs[-1]

arr  = [7,10,4,3,20,15]
k = 3
print(smallest1(arr,k))
print(smallest2(arr,k))