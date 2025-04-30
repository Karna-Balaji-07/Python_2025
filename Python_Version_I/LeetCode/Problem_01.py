# Problem 01 - Two sum problem

''' Approach : 
First we define an empty dictionary. THen we select the elements of the array one by one using loops. 
Then we check if the required exists in the dict ( target - arr[i])
target - arr[i] will return the element which when added with arr[i] equals to target
if that element exists, then return the indexs

dicts[arr[i]] = i   ==> will store the index of each arrray element where elements as key and indexes as values

'''

'''
Approach 1 : 
=> use nested loops
=> THe idea is to get the sum of all the subarrays and then compare it with target.
Time complexity would be O(n2) 
'''
def twoSum1(arr,target):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return [-1,-1]


'''
Approach 2: 
THe idea here is to store the indices of the element in the dictionary as
key : arr[i] key stores the array element
value = i value stores the index of that element

now we check if target-arr[i] is in dictionary since arr[i]+arr[j] = target
if it is in target, we return the vvalue of the [target-arr[i]] from the dictionary 
basically like using a hashmap
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
print(twoSum1(nums,target))