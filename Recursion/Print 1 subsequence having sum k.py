# Print only one subsequences having sum k

def func(index,arr,res, sums,k):
    if index == len(arr):
        if sums == k:
            print(res)
            return True
        return False

    if func(index+1, arr, res + [arr[index]], sums+arr[index],k):
        return True
    if func(index+1,arr,res,sums,k):
        return True

    return False

print(func(0,[1,2,1],[],0,2))

