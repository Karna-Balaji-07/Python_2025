# Equilibrium index

def solution1(arr):
    n = len(arr)
    left = [0]* (n+1)
    right = [0] * (n+1)
    sums = 0
    for i in range(1,len(arr)+1):
        sums += arr[i-1]
        left[i] = sums
    sums = 0
    arr[:] = arr[::-1]
    for i in range(1, len(arr)+1):
        sums += arr[i-1]
        right[i]  = sums
    right[:] = right[::-1]
    print(left)
    print(right)
    for i in range(1,n):
        if left[i-1] == right[i]:
            return i-1

    return -1

def solution2(arr):
    n = len(arr)

    pref = [0] * n
    suff = [0] * n
    pref[0] = arr[0]
    suff[n - 1] = arr[n - 1]
    for i in range(1, n):
        pref[i] = pref[i - 1] + arr[i]
    for i in range(n - 2, -1, -1):
        suff[i] = suff[i + 1] + arr[i]
    for i in range(n):
        if pref[i] == suff[i]:
            return i

    return -1

def solution3(arr):
    n = len(arr)
    total = sum(arr)
    prefix = 0
    for i in range(n):
        suffix= total - prefix - arr[i]
        if suffix == prefix:
            return i
        prefix += arr[i]

    return -1

arr = [1,2,0,3]
result = solution1(arr)
print(result)
