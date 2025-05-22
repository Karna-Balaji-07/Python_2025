# sorted subsequence of size 3

def solution1(arr):
    res = []
    seq = 1
    maxswq = float('-inf')
    mini = arr[0]
    storemin = mini
    if len(arr) < 3:
        return
    for i in range(1,len(arr)):
        if arr[i] == mini:
            continue
        elif arr[i] < mini:
            mini = arr[i]
            continue
        elif arr[i] < maxswq:
            maxswq = arr[i]
            storemin = mini
        elif arr[i] > maxswq:
            if seq == 1:
                storemin = mini
            seq += 1
            if seq == 3:
                return [storemin,maxswq,arr[i]]
        maxswq = arr[i]
    print("No found")

arr  = [12,11,10,5,6,2,30]
print(solution1(arr))