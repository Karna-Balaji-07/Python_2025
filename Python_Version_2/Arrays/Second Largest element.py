# Find the second largest element

def solution1(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

def solution2(arr):

    second = float('-inf')
    first = max(arr)
    for i in arr:
        if i > second and i < first:
            second = i
    return second

def solution3(arr):
    second = -1
    first = -1
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]

        elif arr[i] > second and arr[i] < first:
            second = arr[i]

    return second

arr = [3,9,20,45,75,34,86,65,98]
print(solution1(arr))
print(solution2(arr))
print(solution3(arr))