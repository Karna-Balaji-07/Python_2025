# Intersection of two arrays

def intersection(arr1,arr2):
    result=[]
    for i in arr1:
        if i in arr2 and i not in result:
            result.append(i)
    return result

def intersection1(arr1,arr2):
    arr1=set(arr1)
    arr2=set(arr2)
    result=list(arr1 & arr2)
    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1,nums2))
print(intersection1(nums1,nums2))
