# Array Reversal 

arr = [1,4,2,77,43,54,23,20,10,9]

# method - 1 = in-built method
arr.reverse()
print(arr)

# method - 2 = Using Temporary array

arr = [1,4,2,77,43,54,23,20,10,9]
temp = [0] * len(arr)
for i in range(len(arr)):
    temp[i] = arr[len(arr)-i-1]
print(temp)

arr = [1,4,2,77,43,54,23,20,10,9]
temp = []
for i in range(len(arr)-1,-1,-1):
    temp.append(arr[i])
print(temp)

# method -3 = Using two pointers

arr = [1,4,2,77,43,54,23,20,10,9]
n = len(arr)
left = 0
right = n-1
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print(arr)

