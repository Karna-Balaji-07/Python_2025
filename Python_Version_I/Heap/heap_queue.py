# Heap queue or heapq in python

import heapq 

arr = [10,20,15,30,40]
# heapify function to maintain the property of heap data structure
heapq.heapify(arr)
# adding elements into the heap data strucutre
heapq.heappush(arr,25)
heapq.heappush(arr,5)
heapq.heappush(arr,35)
heapq.heappush(arr,50)
heapq.heappush(arr,45)
# Pops the minimum element from the heap data structure
mini = heapq.heappop(arr)
# appending and popping at the same time
minis = heapq.heappushpop(arr,22)
print(minis)
print(mini)
print(arr)