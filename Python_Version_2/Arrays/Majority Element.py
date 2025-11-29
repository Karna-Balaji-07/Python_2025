# Find the majority element n//2

def solution1(arr):
    n = len(arr)
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for key, values in dicts.items():
        if values > n//2:
            return key

    return -1

def solution2(arr):
    n = len(arr)
    candidate = -1
    count = 0
    for i in arr:
        print("Current Element : ",i)
        if count == 0:
            candidate = i
            print("Candidate : ",candidate)
            count += 1
            print("Count : ",count)
        elif i == candidate:
            count += 1
            print("Count Elif : ",count)
        else:
            count -= 1
            print("Count Else : ",count)
    count = 0
    for i in arr:
        if i == candidate:
            count += 1
    if count > n//2:
        return candidate
    else:
        return -1

arr = [1, 1, 2, 1, 3, 5, 1]
print(solution2(arr))