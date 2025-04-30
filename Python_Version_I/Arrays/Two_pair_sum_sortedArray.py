# Two sum - pair sum in sorted array

def pair(arr, target):
    n = len(arr)
    first = 0
    last = n-1
    arr.sort()
    while first < last:
        sums = arr[first] + arr[last]
        if sums == target:
            return first+1,last+1
        elif sums > target:
            last -= 1
        else:
            first += 1
    return -1

arr = [3,2,4]
print(pair(arr,6))