# Maximum product subarray

def product(arr):
    n = len(arr)
    max_product = arr[0]
    current_min =current_max = arr[0]
    for i in range(1,len(arr)):
        temp = max(arr[i],arr[i]*current_max, arr[i]*current_min)
        current_min = min(arr[i],arr[i]*current_max, arr[i]*current_min)
        current_max = temp
        max_product = max(max_product, current_max)
    return max_product

arr = [-2, 6, -3, -10, 0, 2]
print(product(arr))