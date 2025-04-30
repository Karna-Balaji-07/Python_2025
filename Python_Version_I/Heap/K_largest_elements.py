# K largest elements in the array

# using inbuilt sort function and then return the k largest elements
def solution1(arr,k):
    arr.sort(reverse=True)
    return arr[0:k]

# using heapq property
import heapq
def solution2(arr,k):
    temp = []
    arrs = [-num for num in arr]
    heapq.heapify(arrs)
    for i in range(k):
        maxi = heapq.heappop(arrs)
        temp.append(-1 * maxi)
    return temp

def solution3(arr,k):
    minH = arr[:k]
    heapq.heapify(minH)

    for i in arr[k:]:
        if i > minH[0]:
            heapq.heapreplace(minH,i)
    result = []
    while minH:
        maxi = heapq.heappop(minH)
        result.append(maxi)
    return result
    

arr = [1, 23, 12, 9, 30, 2, 50]
print(solution1(arr,3))
print(solution2(arr,3))
print(solution3(arr,3))