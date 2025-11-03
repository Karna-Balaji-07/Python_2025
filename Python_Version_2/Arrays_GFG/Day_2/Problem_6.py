# 2161. Partition array according to given pivot

def solution1(arr, pivot):
    less = []
    equal = []
    more = []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)
        
    result = []
    result = less + equal + more
    return result

def solution2(arr,pivot):
    start = 0
    end = len(arr)-1
    i = 0
    while i <= end:
        if arr[i] < pivot:
            arr[i],arr[start] = arr[start],arr[i]
            i += 1
            start += 1
        elif arr[i] > pivot:
            arr[i],arr[end] = arr[end],arr[i]
            end -= 1
        else:
            i+= 1
    return arr


nums = [9,12,5,10,14,3,10]
pivot = 10
print(solution2(nums,pivot))