# Kth- Distance duplicates

"""Given an unsorted array that may contain duplicates. Also given a number k which is smaller than the size of the array.
 Write a function that returns true if the array contains duplicates within k distance."""

def kth1(arr,k):
    n = len(arr)
    for i in range(n-k):
        for j in range(i+1,k+1):
            if arr[i] == arr[j]:
                return True
    return False

def kth2(arr,k):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] in temp:
            return True
        temp.append(arr[i])
        if (i >= k):
            temp.remove(arr[i-k])
    return False

arr = [1,2,3,4,1,2,3,4]
arr1 = [1,2,3,1,5,6]
arr2 = [
    6954, 12466, 29875, 19472, 2121, 18273, 16065, 19166, 24382, 2468, 24271, 357, 5584, 31924, 20874, 5299, 11176, 5417,
    7799, 32329, 17424, 31155, 24535, 1138, 3322, 24074, 463, 3283, 5956, 2600, 31941, 32066, 1082, 25013, 3853, 7900,
    11357, 32707, 14789, 14161, 9059, 15035, 1277, 19587, 15742, 9367, 20252, 18000, 31201, 23378, 11134, 25259, 30337,
    15773, 5218, 12274, 20760, 22484, 29700, 379, 6512, 7472, 18694, 4721, 14558, 16702, 27156, 19166, 29452, 17808, 
    11464, 23304, 25596, 4018, 29643, 8449, 8010, 7007, 26686, 3194, 21682, 7413, 25176
]

print(kth1(arr,3))
print(kth1(arr,3))
print(kth1(arr1,3))
print(kth2(arr1,3))
print(kth2(arr2,64))