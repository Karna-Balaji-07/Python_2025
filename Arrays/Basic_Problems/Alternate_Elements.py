# Alternate elements of the array

def alternate(arr):
    n = len(arr)
    for i in range(0,n,2):
        print(arr[i])

arr = [10,20,30,40,50,60]
alternate(arr)