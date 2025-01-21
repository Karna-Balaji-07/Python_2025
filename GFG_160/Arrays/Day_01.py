# Second Largest Element in the array

def second(arr):
    arrs = list(set(arr))
    arrs.sort(reverse=True)
    if len(arrs) == 1:
        return arrs[0]
    else:
        return arrs[1]
    
arr = [10, 10, 10]
arrs = [10, 5, 10]
print(second(arr))
print(second(arrs))