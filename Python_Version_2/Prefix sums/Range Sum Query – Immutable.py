# Range Sum Query – Immutable


def solution(arr,query):
    prefix = [0] * (len(arr)+1)
    for i in range(1,len(arr)+1):
        prefix[i] = prefix[i-1] + arr[i-1]
    print(prefix)
    result = []
    for left, right in query:
        curr = prefix[right+1] - prefix[left]
        result.append(curr)
        print(result)
    return result

arr = [-2, 0, 3, -5, 2, -1]
query  =[[0, 2], [2, 5], [0, 5]]
print(solution(arr, query))
