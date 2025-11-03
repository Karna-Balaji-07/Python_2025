# Find the number that appears once and twice

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for key, values in dicts.items():
        if values  == 1:
            return key

    return -1

def solution2(arr):
    xor = 0
    for i in arr:
        xor ^= i

    return xor