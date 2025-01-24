# Subarray sum equals k

def subarray(arr,k):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i,n):
            if sum(arr[i:j+1])==k:
                count+=1
    return count

def subarray1(arr,k):
    prefix_sum={0:1}
    prefix=0
    count=0
    for i in arr:
        prefix += i
        if prefix-k in prefix_sum:
            count+=prefix_sum[prefix-k]
        if prefix in prefix_sum:
            prefix_sum[prefix] +=1
        else:
            prefix_sum[prefix]=1
    return count

nums = [1,2,3]
k = 3
print(subarray(nums,k))
print(subarray1(nums,k))

