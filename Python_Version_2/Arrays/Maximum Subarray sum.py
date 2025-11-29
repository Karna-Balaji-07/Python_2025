# Maximum subarray sum - Kadane's algorithm

def solution1(arr):
    result = arr[0]
    maxi = arr[0]
    for i in range(1, len(arr)):
        print("Element: ",arr[i])
        maxi = max(arr[i], arr[i]+maxi)
        print("Maxi : ",maxi)
        result = max(result, maxi)
        print("result : ",result)
    return result

arr = [2, 3, -8, 7, -1, 2, 3]
print(solution1(arr))