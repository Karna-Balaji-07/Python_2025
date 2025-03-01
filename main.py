# Prefix ssum

def prefix_sum(arr):
    result = [1]*len(arr)
    for i in range(len(arr)):
        result[i] = sum(arr[:i+1])
    return result

arr = [1,2,3,4,5]
print(prefix_sum(arr))

maximum/minimum in the left
maximum/minimum in the right
suffix sum
prefix sum