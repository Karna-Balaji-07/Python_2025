# Leaders of Arrays

"""You are given an array arr of positive integers.
 Your task is to find all the leaders in the array. 
 An element is considered a leader if it is greater than or equal to all elements to its right. 
 The rightmost element is always a leader."""

def leaders(arr):
    n = len(arr)
    max = -1
    temp = []
    for i in range(n-1,-1,-1):
        if arr[i] >= max:
            temp.append(arr[i])
            max = arr[i]
    temp.reverse()
    return temp

arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))