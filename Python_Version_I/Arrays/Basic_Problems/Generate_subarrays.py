# To Generate all subarrays

def subarrays(arr):
    temp = []
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            temp.append(arr[i:j])
    return temp

def subarrays2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])
        

arr = [1,2,3,4,5]
print(subarrays(arr))
subarrays2(arr)