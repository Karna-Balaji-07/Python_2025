"""this is a two-step process:


The first step gives the element that may be the majority element in the array. If there is a majority element in an array, then this step will definitely return majority element, otherwise, it will return candidate for majority element.
Check if the element obtained from the above step is the majority element. This step is necessary as there might be no majority element. 
Follow the steps below to solve the given problem:

Initialize a candidate variable and a count variable.
Traverse the array once:
If count is zero, set the candidate to the current element and set count to one.
If the current element equals the candidate, increment count.
If the current element differs from the candidate, decrement count.
Traverse the array again to count the occurrences of the candidate.
If the candidate‘s count is greater than n / 2, return the candidate as the majority element.
"""

def majority(arr):
    n = len(arr)
    candidate = 0
    count = 0
    for i in arr:
        if count == 0:
            candidate = i
            count = 1
        elif i == candidate:
            count += 1
        else:
            count -= 1
    count = 0
    for i in arr:
        if i == candidate:
            count += 1
        
    if count > n//2:
        return candidate
    return -1

arr = [3,2,5,3,3]
print(majority(arr))