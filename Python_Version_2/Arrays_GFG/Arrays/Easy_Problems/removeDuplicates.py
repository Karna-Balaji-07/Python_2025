# remove the duplicates from sorted array without using set or hashmap

def solution(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)

    arr[:] = result
    return arr

def solution2(arr):
    n = len(arr)
    if n <= 1:
        return n
    index = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[index] = arr[i]
            index += 1
    return index

arr = [2,2,2,2,2]
print(solution2(arr))