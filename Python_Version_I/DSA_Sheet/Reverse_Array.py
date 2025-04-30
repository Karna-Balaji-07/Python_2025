# Reverse an array
# using inbuilt function reverse()
def inbuill(arr):
    arr.reverse()
    return arr

# Using two pointers
def reverse1(arr):
    left = 0
    n = len(arr)
    right = n-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr

def reverse2(arr):
    n = len(arr)
    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    return arr
arr = [1,5,8,2,5,0,6]
#print(inbuill(arr))
arrs = reverse2(arr)
print(arrs)