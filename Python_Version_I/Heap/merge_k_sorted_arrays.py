# merge k sorted arrays 

def solution1(arr):
    result =[]
    for i in arr:
        result.extend(i)
    result.sort()
    print(result)
    
arr = [[1,2,3],[4,5,6],[7,8,9]]
solution1(arr)