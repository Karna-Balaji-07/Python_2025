# Maximum subarray product

def max_prod(arr):
    n = len(arr)
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    for i in range(1,n):
        num = arr[i]
        if num < 0:
            max_product,min_product = min_product,max_product

        max_product = max(num, num*max_product)
        min_product = min(num , num*min_product)
        result = max(result,max_product)
    return result

arr = [6,-3,10,0,2]
print(max_prod(arr))