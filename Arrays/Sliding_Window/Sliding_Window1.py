# SLIDING WINDOW 1

# MAXIMUM SUM OF ALL SUBARRAYS

def maxsum(arr,k):
    n = len(arr)
    window_sum = sum(arr[:k])
    maxi = window_sum
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        maxi = max(window_sum, maxi)
    return maxi

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
print(maxsum(arr,4))
