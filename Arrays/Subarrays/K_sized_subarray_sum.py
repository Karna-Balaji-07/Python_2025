# Subarray of size k with given sum

def sum1(arr,element,size):
    n = len(arr)
    for i in range(n):
        adds = arr[i]
        for j in range(i+1, size+1):
            adds += arr[j]
            if adds == element:
                return True
    return False

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
size = 4
element = 18
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
size = 3
element = 6
print(sum1(arr,element,size))
