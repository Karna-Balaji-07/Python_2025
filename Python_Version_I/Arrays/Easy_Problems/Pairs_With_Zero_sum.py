# Two sum - Pairs with zero sum

def two_sum(arr):
    arr.sort()
    n = len(arr)
    first=0
    last=n-1
    arrs=[]
    while first<last:
        if arr[first]+arr[last]==0:
            arrs.append([arr[first],arr[last]])
            while first < last and arr[first]==arr[first+1]:
                first+=1
            while first < last and arr[last]==arr[last-1]:
                last-=1
            first+=1
            last-=1
        elif arr[first]+arr[last] > 0:
            last-=1
        elif arr[first]+arr[last] < 0:
            first+=1

    return  arrs

arr=[6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
print(two_sum(arr))