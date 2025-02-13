# Find subsequence of length K with largest sum

import heapq
from collections import Counter
def solution1(arrs,k):
    result = heapq.nlargest(k,arrs)
    count = Counter(result)
    arr = []
    for i in result:
        if count[i] > 0:
            arr.append(i)
            count[i] -= 1
    return result

def solution2(arr,k):
    result = []
    maxarr = sorted(arr,reverse=True)[:k]
    for i in arr:
        if i in maxarr:
            result.append(i)
            maxarr.remove(i)
            if len(maxarr) == 0:
                return result
nums = [33,-27,-9,-83,48]
k=2
print(solution1(nums,k))
print(solution2(nums,k))