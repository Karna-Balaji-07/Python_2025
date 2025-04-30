# Valid Pair Sum

def valid(arr):
    n=len(arr)
    arr.sort()
    count=0
    right=n-1
    left=0
    while right > left:
        sums = arr[left]+arr[right]
        if sums > 0:
            count += (right-left)
            right-=1
        else:
            left += 1
    return count

arr = [3, -2, 1]
print(valid(arr))