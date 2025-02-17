# Maximum distance between two occurrances

def solution1(arr):
    index =0
    max_distace = float('-inf')
    for i in range(len(arr)):
        index = i
        for j in range(i+1,len(arr)):
            if arr[index] == arr[j]:
                res = j - index
                max_distace = max(max_distace,res)

    return max_distace

def solution2(arr):
    dicts = {}
    result = 0
    for i in range(len(arr)):
        if arr[i] not in dicts:
            dicts[arr[i]] = i
        else:
            result = max(result, i - dicts[arr[i]])
    return result

arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
print(solution2(arr))