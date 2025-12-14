# left and right sum queries

def solution1(arr):
    left = [0]*len(arr)
    right = [0] * len(arr)

    for i in range(1, len(arr)):
        left[i] = left[i-1] + arr[i-1]
        print(f'Left[i] = {left[i]}')
    for i in range(len(arr)-2,-1,-1):
        right[i] = right[i+1] + arr[i+1]
    print("Left array : ",left)
    print("Right array : ", right)
    result = []
    for i in range(len(arr)):
        result.append(abs(left[i]-right[i]))
    return result

nums = [10,4,8,3]
print(solution1(nums))