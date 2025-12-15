# subarray sum with zero sum

def solution(arr):
    n = len(arr)
    prefix = 0
    s = set()
    for i in range(n):
        prefix += arr[i]
        if prefix == 0 or prefix in s:
            return True
        s.add(prefix)

    return False