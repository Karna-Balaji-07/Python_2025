# Count the number of subarrays with the given XOR k

def solution1(arr,k):
    dicts = {}
    prefix = 0
    result = 0
    for i in range(len(arr)):
        prefix ^= arr[i]
        if prefix == k:
            result += 1

        if prefix ^ k in dicts:
            result += dicts[prefix^k]

        dicts[prefix] = dicts.get(prefix,0)+1

    return result
A = [5, 6, 7, 8, 9]; k = 5
print(solution1(A,k))