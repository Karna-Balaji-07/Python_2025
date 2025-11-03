# Check if the array is sorted or not

def solution1(arr):
    flag = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            flag = False
            break
    if flag == False:
        print(f'Array is not sorted')
    else:
        print(f'Array is sorted')

def solution2(arr):
    arrs = sorted(arr)
    if arrs == arr:
        print('Sorted')
    else:
        print('Not sorted')


arr = [1,3,5,7,9]
arrs = [1,3,5,7,3]
solution1(arr)
solution1(arrs)
solution2(arrs)
solution2(arr)