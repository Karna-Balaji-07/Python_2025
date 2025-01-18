# apartments problem

def apartments(people,apt,k,n,m):
    i,j=0,0
    count=0
    apt.sort()
    people.sort()

    while i < n  and j<m:
        if abs(people[i]-apt[j]) <= k:
            count+=1
            i+=1
            j+=1
        elif apt[j] < people[i]-k:
            j+=1
        else:
            i+=1
    return count
    
    
n,m,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
result = apartments(arr1,arr2,k,n,m)
print(result)