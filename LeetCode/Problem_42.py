# Trapping Rain Water

# approach 1 : finding the left max and right max
def trap1(arr):
    result = 0
    for i in range(1,len(arr)-1):
        # Find the left max
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # find the right max
        right = arr[i]
        for j in range(i+1, len(arr)):
            right = max(right, arr[j])

        # Find the minimum among left max and right max
        # and difference it with the current element
        result += (min(left,right)) - arr[i]

    return result

def trap2(arr):
    left = 1
    right = len(arr)-2
    lmax = arr[left-1]
    rmax = arr[right+1]
    result = 0
    while left <= right:
        if rmax <= lmax:
            result += max(0,rmax-arr[right])
            rmax = max(rmax, arr[right])
            right -= 1
        else:
            result += max(0, lmax-arr[left])
            lmax = max(lmax,arr[left])
            left +=1
    return result

def trap3(  )

arr = [2, 1, 5, 3, 1, 0, 4]
print(trap2(arr))