# stock buy and sell where multiple transcations allowed

def stocks1(arr):
    n = len(arr)
    maxima = arr[0]
    minima = arr[0]
    res = 0
    i=0
    while i < n-1:
        while i < n-1 and arr[i] >= arr[i+1]:
            i+=1
        minima = arr[i]

        while i < n-1 and arr[i] <= arr[i+1]:
            i += 1
        maxima = arr[i]

        res+=maxima-minima
    return res


def stocks2(arr):
    n=len(arr)
    res=0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            res += arr[i]-arr[i-1]
    return res

prices = [100, 180, 260, 310, 40, 535, 695]
print(stocks1(prices))
print(stocks2(prices))