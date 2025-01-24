# Search in Rotated Sorted Array

def rotated(arr,target):
    for i in range(len(nums)):
        if arr[i] == target:
            return i
    return -1

nums = [4,5,6,7,0,1,2]
print(rotated(nums,3))
        