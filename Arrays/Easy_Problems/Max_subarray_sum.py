# Maximum sum of subarray

def subsum1(arr):
    n = len(arr)
    i,j = 0,1
    sum = 0
    while i < n and j < n:
        sum += arr[i:j]
        if sum < 0:
            i = j
            j = j+1
        else:
            j+=1
        i += 1
    return sum

arr = [2,3,-8,7,-1,2,3]
print(subsum1(arr))

