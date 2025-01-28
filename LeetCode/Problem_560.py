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

def subarray2(arr,k):
    sums = 0
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    
    result=0
    dicts={0:1}
    for i in arr:
        target = i-k
        if target in dicts:
            result += dicts[target]
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i]=1
    return result


        

nums = [1,2,3]
k = 3
print(subarray(nums,k))
print(subarray1(nums,k))

