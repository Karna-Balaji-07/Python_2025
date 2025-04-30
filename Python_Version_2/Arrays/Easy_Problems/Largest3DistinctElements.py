# Largest 3 distinct elements in an array

def solution1(arr):
    arrs = list(set(arr))
    arrs.sort(reverse=True)
    return arrs[:3]

def solution2(arr):
    result = []
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    for i in arr:
        if i > first:
            first = i
    result.append(first)
    for i in arr:
        if i > second and i != first:
            second = i
    result.append(second)
    for i in arr:
        if i > third and i != first and i != second:
            third = i
    result.append(third)
    return result

arr = [10, 4, 3, 50, 23, 90, 90]
print(solution2(arr))