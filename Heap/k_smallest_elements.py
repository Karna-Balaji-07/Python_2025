# K smalest elements in an array

# using inbuilt sort function and then return the first k smallest elements
def solution1(arr,k):
    arr.sort()
    return arr[:k]

#using minheap
import heapq
def solution2(arr,k):
    heapq.heapify(arr)
    result = []
    for i in range(k):
        mini = heapq.heappop(arr)
        result.append(mini)
    return result

def solution3(arr,k):
    heap = []
    for i in arr:
        heapq.heappush(heap,i)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

arr = [1, 23, 12, 9, 30, 2, 50]

print(solution3(arr,3))