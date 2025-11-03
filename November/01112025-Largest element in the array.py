# Find the first, second and third largest element in the array

def solution1(arr):
    n = len(arr)
    arr = list(set(arr))
    arr.sort()
    print(f'First largest : {arr[-1]}')
    print(f'Second largest : {arr[-2]}')
    print(f'Third largest : {arr[-3]}')

def solution2(arr):
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    for i in arr:
        if i > first:
            first = i

    for i in arr:
        if i > second and i < first:
            second = i

    for i in arr:
        if i > third and i < second and i < first:
            third = i

    print(f'Frist largest : {first}')
    print(f'Second largest : {second}')
    print(f'Third largest : {third}')

arr = [3,6,8,1,3,9,4,6,2,4,3,5,8,9,10,13,15,376,454,23,73,13]
solution1(arr)
solution2(arr)