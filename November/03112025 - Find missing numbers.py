# Find missing numbers

def solution1(arr):
    n = len(arr)
    arr.sort()
    for i in range(1, n+1):
        if i != arr[i-1]:
            return i

    return  -1

def solution2(arr):
    n = len(arr)
    arr.sort()
    for i in range(n+1):
        if i not in arr[i]:
            return i
    return -1

def solution3(arr):
    sums = sum(arr)
    n = len(arr)
    return n*(n+1) // 2 - sums

arr = [1,0]
print(solution3(arr))