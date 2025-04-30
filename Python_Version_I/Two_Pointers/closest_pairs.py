# Closest pairs

def closest(arr1, arr2,target):
    n = len(arr1)
    m = len(arr2)
    left= 0
    right = m-1
    diff = float('inf')
    while left < n and right > 0:
        if abs(arr1[left]+arr2[right]-target) < diff:
            lefts = left
            rights = right
            diff = abs(arr1[left]+arr2[right]-target)
        if abs(arr1[left]+arr2[right]) > target:
            right -= 1
        else:
            left += 1
    return list((arr1[lefts],arr2[rights]))

arr = [1,4,5,7]
brr = [10,20,30,40]
print(closest(arr,brr,32))
