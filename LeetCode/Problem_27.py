# Remove the element

def remove(arr,key):
    arrs = []
    for i in arr:
        if i != key:
            arrs.append(i)
    arr[:] = arrs
    return arr

