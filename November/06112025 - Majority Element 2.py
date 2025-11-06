# Majority element n/3

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for key, value in dicts.items():
        if value > len(arr)//3:
            return key

    return -1


def solution2(arr):
    candidate = -1
    n = len(arr)
    count = 0
    for i in arr:
        if count == 0:
            candidate = i
            count = 1

        elif i == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for i in arr:
        if i == candidate:
            count += 1

    if count > n//3:
        return candidate
    else:
        return -1