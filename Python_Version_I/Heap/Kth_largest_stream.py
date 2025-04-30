# Kth largest in a stream

import heapq
def solution(arr,k,n):
    result = [-1]*n
    for i in range(k-1,n):
        indexed = i - k + 1
        result[i] = arr[indexed]

    print(result)

def solution2(arr,k,n):
    result = []
    heap = []
    for i in range(n):
        heapq.heappush(heap,arr[i])
        if len(heap) > k:
            heapq.heappop(heap)
        if len(heap) < k:
            result.append(-1)
        else:
            result.append(heap[0])
    return result

arr = [1,2,3,4,5,6]
k = 4
n = 6
print(solution2(arr,k,n))