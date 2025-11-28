# Count all subsequences having sum k

def func(index, arr, sums, k, take= 0, nottake=0):
    if index == len(arr):
        return 1 if sums  == k else 0

    take += func(index+1, arr, sums+arr[index],k)
    nottake += func(index+1,arr,sums,k)
    return take + nottake

arr = [1,2,1]
k = 2
print(func(0,arr,0,k))