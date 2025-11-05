# Find the duplicate in an array of n+1 integers

def solution1(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]

    return -1

def solution2(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

def solution3(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for key, values in dicts.items():
        if values == 2:
            return key

    return -1


arr = [1,3,4,2,2]
print(solution1(arr))