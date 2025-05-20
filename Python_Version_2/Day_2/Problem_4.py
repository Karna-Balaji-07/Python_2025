# 2200 . Find all K-Distant indices in an array

def solution1(arr,key,k):
    index = []
    for i in range(len(arr)):
        if arr[i] == key:
            index.append(i)
    i = 0
    j = 0
    result = []
    for i in range(len(arr)):
        for j in index:
            if abs(i-j) <= k:
                result.append(i)
                break
    return result

arr = [2,2,2,2,2]
key = 2
k = 2
print(solution1(arr,key,k))