# Minimum and maximum in an array

def min_max(arr):
    mini = float('inf')
    maxi = float('-inf')
    for i in arr:
        if i > maxi:
            maxi = i
    for i in arr:
        if i < mini:
            mini = i

    return maxi, mini

A = [4, 9, 6, 5, 2, 3]
print(min_max(A))