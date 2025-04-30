'''
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
'''

def solution2(arr):
    for i in range(len(arr)):
        arr[i].sort(reverse=True)

    result = 0
    for i in range(len(arr[0])):
        value = arr[0][i]
        for j in range(1,len(arr)):
            value = max(value, arr[j][i])
        result += value
    return result

arr = [[1, 2, 4], [3, 3, 1]]
print(solution2(arr))