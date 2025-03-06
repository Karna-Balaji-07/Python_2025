# Peak element

def peak(arr):
    maxi = max(arr)
    return arr.index(maxi)

arr = [1,2,1,3,5,6,4]
print(peak(arr))