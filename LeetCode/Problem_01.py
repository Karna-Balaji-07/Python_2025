# Problem 01 - Two sum problem

''' Approach : 
First we define an empty dictionary. THen we select the elements of the array one by one using loops. 
Then we check if the required exists in the dict ( target - arr[i])
target - arr[i] will return the element which when added with arr[i] equals to target
if that element exists, then return the indexs

dicts[arr[i]] = i   ==> will store the index of each arrray element where elements as key and indexes as values

'''

def twoSum(arr,target):
    n = len(arr)
    dicts = {}
    for i in range(len(arr)):
        if target - arr[i] in dicts:
            return [dicts[target-arr[i]],i]
        dicts[arr[i]] = i
    return [-1,-1]


nums = [3,2,4]
target = 6
print(twoSum(nums,target))