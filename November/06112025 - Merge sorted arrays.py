# Merge sorted arrays without using extra space

def solution1(arr1, arr2,n,m):
    i = n-1
    j = m-1
    k = i+j-1
    while i >= 0 and j >= 0:
        if arr1[i] >arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1


    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

    return arr1