# Left rotate the array by K places

def solution1(arr,k):
    n = len(arr)
    k %= n
    arr[:] = arr[k:]+arr[:k]
    print(arr)

def solution2(arr,k):
    k %= len(arr)
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    arr.reverse()
    print(arr)

arr = [1,2,3,4,5]
solution1(arr,1)
solution2(arr,0)