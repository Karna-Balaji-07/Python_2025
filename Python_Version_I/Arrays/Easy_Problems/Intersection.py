# Intersection of two arrays

def intersection(arr1,arr2):
    result=[]
    for i in arr1:
        if i in arr2:
            result.append(i)
            arr2.remove(i)
    return result

arr1 = [1, 2, 3, 4]
arr2 = [ 6, 7, 8]
print(intersection(arr1,arr2))