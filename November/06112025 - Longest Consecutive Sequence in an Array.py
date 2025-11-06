# Longest common subsequence in an array
from Python_Version_I.Revision.CSE358_CA_revision import last_element


def solution1(arr):
    arr = list(set(arr))
    arr.sort()
    count = 1
    result = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]+1:
            count += 1
            print("Count : ",count)
        else:
            result = max(count, result)
            count = 1
            print("Result : ",result)
        result = max(count, result)
    return result

def solution2(arr):
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()
    lastsmaller = float('inf')
    count = 0
    longest = 1
    for i in range(n):
        if arr[i] - 1 == lastsmaller:
            count += 1
            lastsmaller = arr[i]
        elif arr[i] != lastsmaller:
            count = 1
            lastsmaller = arr[i]

        longest = max(count, longest)
    return longest


arr = [1,0,1,2]
print(solution1(arr))