# Search an element in a strictly sorted 2d array

def search1(arr, element):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == element:
                return True
    return False

# Using binary search
def search2(arr, element):
    n = len(arr)
    m = len(arr[0])
    low = 0
    high = n*m-1
    while low <= high:
        mid = (low+high) // 2
        row = mid // m
        col = mid % m
        if arr[row][col] == element:
            return True
        elif arr[row][col] < element:
            low = mid +1
        elif arr[row][col] > element:
            high = mid -1
    return False

mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
element = 14
print(search1(mat, element))
print(search2(mat,element))

