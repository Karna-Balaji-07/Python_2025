# next greater element in an array

def greater_element(nums):
    stack = []
    n = len(nums)
    result = [-1]*n
    for num in range(n-1,-1,-1):
        while stack and nums[num]>=nums[stack[-1]]:
            stack.pop()
        if stack:
            result[num] = nums[stack[-1]]
        stack.append(num)
    return result
    
arr = [6, 8, 0, 1, 3]
print(greater_element(arr))