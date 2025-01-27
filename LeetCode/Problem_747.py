# Largest number at least twice of others

def largest(arr):
    n=len(arr)
    max_element=0
    for i in range(1,n):
        if arr[i] > arr[max_element]:
            max_element=i
        
    for i in range(n):
        if max_element != i and arr[max_element] < arr[i]*2:
            return -1
    return max_element

arr = [3,6,1,0]
print(largest(arr))

        