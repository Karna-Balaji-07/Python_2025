# Range sum query

def solution1(arr, query):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    result = []
    for i, j in query:
        pos = prefix[j] - (prefix[i-1] if i > 0 else 0)
        result.append(pos)
    return result

arr = [-2,0,3,-5,2,-1]
query = [[0, 2], [2, 5], [0, 5]]
print(solution1(arr, query))