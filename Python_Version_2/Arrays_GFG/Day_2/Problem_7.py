# 15. 3 SUM problem - Triplet sum in an array

def solution1(arr):
    dicts = {}
    ans = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            val = -1 * (arr[i] + arr[j])
            if val in dicts:
                for k in dicts[val]:
                    ans.append([k,i,j])
        if arr[i] not in dicts:
            dicts[arr[i]] = []
        dicts[arr[i]].append(i)
    return ans

def solution2(arr):
    arr.sort()
    ans = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
            
        left = i+1
        right = len(arr)-1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                ans.append([arr[i],arr[left],arr[right]])
                while  left  < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return ans

nums = [-1,0,1,2,-1,-4]
print(solution2(nums))