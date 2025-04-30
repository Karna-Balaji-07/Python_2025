# merge 2d arrays by summing the values

def solution1(arr1,arr2):
    arr = nums1 + nums2
    dicts = {}
    for key,value in arr:
        if key in dicts:
            dicts[key] += value
        else:
            dicts[key] = value
    arrs = [[key,value] for key,value in sorted(dicts.items())]
    return arrs


nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

print(solution1(nums1,nums2))
