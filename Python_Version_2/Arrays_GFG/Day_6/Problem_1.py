# Minimums swaps to sort the array

def solution1(arr):
    dicts = {}
    temp = sorted(arr)
    for i in range(len(arr)):
        dicts[arr[i]] = i
    
    swap = 0
    for i in range(len(arr)):
        if temp[i] != arr[i]:
            index = dicts[temp[i]]
            arr[i],arr[index] = arr[index],arr[i]
            dicts[arr[i]] = i
            dicts[arr[index]] = index
            swap += 1
    return swap

arr = [10, 19, 6, 3, 5]
print(solution1(arr))



