# Minimum Number Game

import heapq
def solution1(arr, result):
    heapq.heapify(arr)
    while arr:
        element1 = heapq.heappop(arr)
        element2 = heapq.heappop(arr)
        result.append(element2)
        result.append(element1)
    return result

nums = [5,4,2,3]
result = []
print(solution1(nums,result))
