# Smallest subarray with sum greater than a given value

def smallest1(arr,element):
    start = 0
    n = len(arr)
    end = 0
    sums = 0
    ans = float('inf')
    while end < n:
        while end < n and sums <= element:
            sums += arr[end]
            end += 1
        if end == n and sums <= element:
            break
        while start < end and sums - arr[start] > element:
            sums -= arr[start]
            start += 1
        ans = min(ans,end-start)
        sums -= arr[start]
        start += 1

    if ans == float('inf'):
        return 0
    return ans

arr = [1, 4, 45, 6, 10, 19]
x = 51

print(smallest1(arr,x))

