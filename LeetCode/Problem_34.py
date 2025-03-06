def leftsearch(arr, target):
    first = 0
    last = len(arr)-1
    first_occurence = -1
    while first <= last:
        mid = (first+last) // 2
        if arr[mid] == target:
            first_occurence = mid
            last = mid-1
        elif arr[mid] > target:
            last = mid - 1
        else:
            first = mid + 1
    return first_occurence

def rightsearch(arr, target):
    first = 0
    last = len(arr) - 1
    last_occurance = -1
    while first <= last:
        mid = (first+last)//2
        if arr[mid] == target:
            last_occurance = mid
            first = mid + 1
        elif arr[mid] > target:
            last = mid - 1
        else:
            first = mid+1
    return last_occurance

def mains(arr, target):
    left = leftsearch(arr, target)
    right = rightsearch(arr, target)
    if left == -1 or right == -1:
        return [-1,-1]
    else:
        return [left,right]
arr = [5,7,7,8,8,10]
target = 8
print(mains(arr, target))
