# majority element

def majority1(arr):
    dicts={}
    n=len(arr)
    for i in arr:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i]=1
    for key,value in dicts.items():
        if value > n//2:
            return key
    return -1

def majority2(arr):
    arr.sort()
    return (arr[len(arr)/2])

nums = [2,2,1,1,1,2,2]
print(majority1(nums))
print(majority2(nums))