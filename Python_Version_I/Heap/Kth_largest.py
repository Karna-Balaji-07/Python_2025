# Kth largest element in an array

# using inbuilt sorting algorithm and then returning the kth largest element from the arr
def solution1(arr,k):
    arr.sort()
    return arr[-k]

# using max Heap
import heapq
def solution2(arr,k):
    arrs = [-num for num in arr]
    heapq.heapify(arrs)
    result = []
    for i in range(k):
        result.append(heapq.heappop(arrs))
    return -(result[-1])

arr = [1, 23, 12, 9, 30, 2, 50]
print(solution1(arr,3))
print(solution2(arr,3))