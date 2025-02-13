# Minimum cost of ropes

import heapq
def solution1(arr):
    heapq.heapify(arr)
    result = []
    if len(arr) == 1:
        return 0
    else:
        while arr:
            element1 = heapq.heappop(arr)
            element2 = heapq.heappop(arr)
            add = element1+element2
            heapq.heappush(arr,add)
            result.append(add)
            if len(arr) == 1:
                break
    return sum(result)

arr = [4, 3, 2, 6]
print(solution1(arr))