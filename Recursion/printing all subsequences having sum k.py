# Print all the subsequences having sum k

def func(index,arr,res, sums,k):
    if index == len(arr):
        if sums == k:
            print(res)
        return

    func(index+1, arr, res+[arr[index]], sums+arr[index],k)
    func(index+1, arr,res,sums,k)

arr = [1,2,1]
k = 2
res = []
func(0,arr,res,0,k)
