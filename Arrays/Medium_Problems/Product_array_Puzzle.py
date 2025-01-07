#  Product array puzzle

def product(arr):
    n = len(arr)
    prod = [1] *n
    for i in range(n):
        for j in range(n):
            if i != j:
                prod[i] *= arr[j]
    return prod

def product2(arr):
    n = len(arr)
    result = [1] * n
    left = [1]*n
    right = [1]*n
    for i in range(1,n):
        left[i] = left[i-1] * arr[i-1]
    for i in range(n-2,-1,-1):
        right[i] = arr[i+1] * right[i+1]
    for i in range(n):
        result[i] = left[i] * right[i]
    return result

arr = [4, 6, 8, 0, 2, 5, 5, 3, 2, 8, 1]
print(product(arr))
print(product2(arr))
 