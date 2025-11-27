# Remove all occurrences of that element in the array

def solution1(arr,element):
    n = len(arr)
    index = 0
    for i in range(n):
        if arr[i] != element:
            arr[index] = arr[i]
            index += 1

    return arr[:index]

arr = [3,2,2,3,2,3]
print(solution1(arr,3))