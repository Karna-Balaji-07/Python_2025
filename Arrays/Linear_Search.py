# Linear Search algorithm

def LinearSearch(arr,element):
    for i in arr:
        if i == element:
            return arr.index(i)
    return -1

def Linear(arr,element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

arr = [1,4,9,16,25,36,49]
element = 36
print(LinearSearch(arr,element))
