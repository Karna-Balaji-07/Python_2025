# Program to generate all the subarrays

def solution1(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            result.append(arr[i:j+1])
    return result

arr = [1,2,3]
print(solution1(arr))