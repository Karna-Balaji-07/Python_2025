'''
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''

def solution1(arr):
    arr.sort(reverse=True)
    num1 = arr[0]-1
    num2 = arr[1]-1
    return num1 * num2

import heapq
def solution2(arr):
    arrs = [-num for num in arr]
    heapq.heapify(arrs)
    result = []
    for i in range(2):
        result.append(-(heapq.heappop(arrs)))

    prod = 1
    for i in result:
        prod *= i-1
    return prod

nums = [3,4,5,2]
print(solution1(arr=nums))
print(solution2(arr=nums))