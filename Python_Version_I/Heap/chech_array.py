# Check if the given array is a binary max heap



def binary1(arr,i,n):
    if i >= int((n-1)/2):
        return True
    
    if arr[i] >= arr[2*i+1] and arr[i] >=arr[2*i+2] and binary1(arr,2*i+1,n) and binary1(arr, 2*i+2,n):
        return True
    return False

def binary2(arr,n):
    for i in range(int((n-2)/2)+1):
        if arr[2*i+1] > arr[i]:
            return False
        if 2*i+2 < n and arr[2*i+2] > arr[i]:
            return False
    return True
arr = [90, 15, 10, 7, 12, 2, 7, 3] 
print(binary1(arr,0,len(arr)))