# 3 sum problem

def threeSum(arr,target):
    dicts={}
    reset = set()
    for i in range(len(arr)):
        for j in range (i+1,len (arr)) :
            sums=arr[i]+arr[j]
            if sums not in dicts:
                dicts[sums]=[]
            dicts[sums].append((i,j))
    for i in range(len(arr)):
        rem = target-arr[i]
        if rem in dicts:
            for p in dicts[rem]:
                if p[0] != i and p[1]!=i:
                    curr=sorted([p[0],p[1],i])
                    reset.add(tuple(curr))
    result=[]
    for i in reset:
        result.append(list(i))
    return result


def threesum(arr):
    target=0
    arr.sort()
    reset = set()
    n=len(arr)
    result=[]
    for i in range(n):
        j=i+1
        k=n-1
        while j < k:
            sums=arr[i]+arr[j]+arr[k]
            if sums == 0:
                reset.add((arr[i],arr[j],arr[k]))
                k -=1
                j+=1
            elif sums < 0:
                j +=1
            else:
                k -=1
    output=list(reset)
    return output





arr = [-1,0,1,2,-1,-4]
target = 0
print(threeSum(arr,target))
print(threesum(arr))

