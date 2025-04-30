# Rotate array by one
'''
Input: arr[] = [1, 2, 3, 4, 5] 
Output: [5, 1, 2, 3, 4]


Input: arr[] = [2, 3, 4, 5, 1]
Output: [1, 2, 3, 4, 5]


'''

def solution1(arr):
    last_element = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last_element
    return arr

def solution2(arr):
    temp = []
    for i in range(len(arr)-1):
        temp.append(arr[i])
    for j in range(len(arr)-1,len(arr)):
        temp.append(arr[j])
    return temp

def solution3(arr):
    first = 0
    last = len(arr)-1
    while first != last:
        arr[first],arr[last] = arr[last],arr[first]
        first += 1
    return arr

def solution4(arr):
    n = len(arr)
    arr[:n-2].reverse()
    arr.reverse()
    return arr

arr = [2, 3, 4, 5, 1]
print(solution1(arr))
print(solution2(arr))
print(solution3(arr))
print(solution4(arr))
