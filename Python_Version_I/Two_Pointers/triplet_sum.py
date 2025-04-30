# Triplet sum

def triplet(arr,target):
    n = len(arr)
    arr.sort()
    for i in range(n-2):
        left = i+1
        right = n-1
        sums = target - arr[i]
        while left < right:
            if arr[left]+arr[right] == sums:
                return True
            if arr[left]+arr[right] > target:
                right -= 1
            else:
                left += 1
    return False

arr = [1,4,45,6,8,10]
print(triplet(arr,13))