# Factory Machines

def check_method(mid,n,t,arr):
    sums = 0
    for i in range(n):
        sums += (mid//arr[i])
        if sums >= t:
            return True
    return False

def factory_machines(n,t,arr):
    low=1
    high=min(arr)*t
    ans = 0
    while low <= high:
        mid = (low+high)//2
        if check_method(mid,n,t,arr):
            ans=mid
            high= mid-1
        else:
            low = mid+1
    return ans

arr=zip(int,input().split())    
n=int(input())
t=int(input())
print(factory_machines(n,t,arr))
