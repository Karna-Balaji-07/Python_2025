# Product of array except self

def product1(arr):
    n=len(arr)
    result=[1]*n
    left = [1]*n
    right = [1]*n
    for i in range(1,n):
        left[i] = left[i-1] * arr[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1]*arr[i+1]
    for i in range(n):
        result[i]=left[i]*right[i]
    return result

def product2(arr):
    n=len(arr)
    result=[1]*n
    start=1
    end=1
    for i in range(n):
        result[i]=start
        start *= arr[i]
    for i in range(n-1,-1,-1):
        result[i] *= end
        end *= arr[i]
    return result



nums = [1,2,3,4]
print(product1(nums))
print(product2(nums))