# Check if subarray with given product exists in an array

def product1(arr,element):
    n = len(arr)
    prod = 1
    for i in range(n):
        prod = arr[i]
        for j in range(i+1,n):
            prod *= arr[j]
            if prod == element:
                return True
    return False

def product2(arr,element):
    n = len(arr)
    start = 0
    prod = 1
    for end in range(n):
        prod *= arr[end]

        while( start <= end and prod == 0 and element != 0):
            start += 1
            prod = 1
            for i in range(start,end+1):
                prod*=arr[i]
        
        while (start <= end and prod != 0 and abs(prod) > abs(element)):
            prod //= arr[start]
            start += 1
        if prod == element:
            return True
    return False

arr = [-2,-1,3,4,-1]
element = 2
print(product1(arr,element))
print(product2(arr,element))