# Longest subarray with sum k

def subarray(arr,key):
    n = len(arr)
    length=0
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            sums = sum(arr[i:j+1])
            if sums == key:
                length = max(length,j-i+1)
    return length


def subarray1(arr, key):
    prefix_sum  = {0:-1}
    currsum= 0
    ans=0
        
    for i in range(len(arr)):
        currsum += arr[i]
        if currsum - key in prefix_sum:
            ans = max(ans, i-prefix_sum[currsum-key])
        if currsum not in prefix_sum:
            prefix_sum[currsum] = i
    return ans
arr =[-5, 8, -14, 2, 4, 12]
key = -5
print(subarray1(arr,key))      
