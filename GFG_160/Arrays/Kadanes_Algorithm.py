# kadane's Algorithm
'''
maximum sum of a subarray
'''

def kadane(arr):
    n = len(arr)
    sums = arr[0]
    maximum = arr[0]
    for i in range(1,len(arr)):
        sums = max(arr[i],sums+arr[i])
        maximum = max(maximum,sums)
    return maximum

arr = [2, 3, -8, 7, -1, 2, 3]
print(kadane(arr))