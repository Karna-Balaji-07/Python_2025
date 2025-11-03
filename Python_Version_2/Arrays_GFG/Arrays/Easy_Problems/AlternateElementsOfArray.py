# Alternate elements of Array

def alternate(arr):
    result = []
    for i in range(0,len(arr),2):
        result.append(arr[i])
    return result

def recursion(arr,index,result):
    if index < len(arr):
        result.append(arr[index])
        recursion(arr, index+2, result)
def mains(arr):
    result = []
    recursion(arr,0,result)
    return result

arr = [1,2,3,4,5,6,7,8,9]
print(alternate(arr))
print(mains(arr))