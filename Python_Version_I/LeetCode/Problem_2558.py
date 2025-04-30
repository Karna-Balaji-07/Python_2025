# Take gifts from the richest pile

import math as m
import heapq
def solution1(arr,k):
    arrs = [-num for num in arr]
    heapq.heapify(arrs)
    for i in range(0,k):
        element = -heapq.heappop(arrs)
        square = m.sqrt(element)
        heapq.heappush(arrs,-int(square))
    
    
    return sum(-num for num in arrs)
    
gifts = [25,64,9,4,100]
k = 4
print(solution1(gifts,k))