# Find the majority element that occurs n /2 times

def solution1(arr):
    n  = len(arr)
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1

    for key, value in dicts.items():
        if value > n//2:
            return key

    return -1