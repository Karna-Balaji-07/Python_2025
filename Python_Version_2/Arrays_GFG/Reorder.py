# Reorder an array according to given indexes

def reorder(arr,indexs):
    n = len(arr)
    arrs = [0]*n
    for i in range(n):
        arrs[i] = arr[indexs[i]]
    
    return arrs

arr = [1,2,3,4]
index = [3,2,0,1]
print(reorder(arr,index))
