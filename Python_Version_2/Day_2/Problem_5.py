# 1. Two sum Problem

def solution1(arr,target):
    s = set()
    for i in arr:
        complement = target  - i
        if complement in arr:
            return True
        s.add(i)
    return False

def solution2(arr,target):
    dicts = {}
    for i,num in enumerate(arr):
        comp = target - num
        if comp in dicts:
            return [dicts[comp], i]
        dicts[num] = i
    
    return []

arr = [2,7,11,15]
target = 9
print(solution2(arr,target=target))