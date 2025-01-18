# Missing number 

def missing(n,arr):
    sums = n * (n+1)//2
    sums1 = sum(arr)
    return sums - sums1

n = int(input())
arr=[]
arr = list(map(int,input().split()))
print(missing(n,arr))