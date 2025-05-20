# Rearrange Array Elements by Sign

def solution1(arr):
    pos = []
    neg = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
        
    index = 0
    posind = 0
    negind = 0

    while posind < len(pos) and negind < len(neg):
        if index % 2 == 0:
            arr[index] = pos[posind]
            posind += 1
        else:
            arr[index] = neg[negind]
            negind += 1
        index += 1

    while posind < len(pos):
        arr[index] = pos[posind]
        posind += 1
    while negind < len(neg):
        arr[index] = neg[negind]
        negind += 1
    return arr

def solution2(arr):
    positive = 0
    negative = 1
    n = len(arr)
    result = [0]*n
    for i in range(n):
        if arr[i] < 0:
            result[negative] = arr[i]
            negative += 2
        else:
            result[positive] = arr[i]
            positive += 2
        
    return result

'''arr = [1, 2, 3, -4, -1, 4] 
print(solution2(arr))
'''
from typing import List

def RearrangebySign(A: List[int]) -> List[int]:
    n = len(A)
    
    # Define array for storing the ans separately.
    ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        # Fill negative elements in odd indices and inc by 2.
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2
        
        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = A[i]
            posIndex += 2
    
    return ans
    
# Test the function
A = [1,2,-4,-5]
ans = RearrangebySign(A)
print(ans)