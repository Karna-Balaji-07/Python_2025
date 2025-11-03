# to check whether the array is sorted or not

def solution1(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            return False
        
    return True


arr = [1,2,3,4,5,6]
print(solution1(arr))
arr = [1,2,3,6,4,8,5]
print(solution1(arr))