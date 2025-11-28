# Third largest element

def solution1(arr):
    first = max(arr)
    second = -1
    third = -1
    for i in arr:
        if i > second and i <  first:
            second = i
    for i in arr:
        if i > third and i < second:
            third = i
    return third

def solution2(arr):
    first = -1
    second = -1
    third = -1
    for i in range(len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] < second:
            third = arr[i]

    return third

arr = [3,9,20,45,75,34,86,65,98]
print(solution1(arr))
print(solution2(arr))