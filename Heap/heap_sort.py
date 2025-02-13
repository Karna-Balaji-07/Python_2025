# Heap sort

import heapq
def solution1(arr):
    result = []
    heapq.heapify(arr)
    while arr:
        ele = heapq.heappop(arr)
        result.append(ele)
    return result

arr = [6,3,4,9,1,3]
print(solution1(arr))