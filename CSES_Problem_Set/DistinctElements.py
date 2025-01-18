# Number of distinct elements in the array

def distinct(arr,n):
    arr.sort()
    arrs= list(set(arr))
    return len(arrs)

n = int(input())
arr = list(map(int,input().split()))

print(distinct(arr,n))
