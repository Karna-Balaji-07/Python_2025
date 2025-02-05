# Next greater element I

def greater(arr1,arr2):
    result = [-1]*len(arr1)
    k=0
    for i in arr1:
        j = arr2.index(i)
        if j+1 < len(arr2) and arr2[j+1] > i:
            result[k] = arr2[j+1]
            
        k += 1

    return result

def greater1(arr1, arr2):
    next_greater = {}
    stack= []
    for num in arr2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    results = []
    for num in arr1:
        results.append(next_greater.get(num,-1))
    return results
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(greater1(nums1,nums2))
