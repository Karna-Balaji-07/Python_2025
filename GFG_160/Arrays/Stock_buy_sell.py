# Stock buy and sell - Maximum One transcation allowed

def transaction(arr):
    n = len(arr)
    if n < 2:
        return 0
    maximum = 0
    minimum = arr[0]
    for i in range(1,n):
        minimum = min(minimum,arr[i])
        maximum = max(maximum, arr[i]-minimum)
    return maximum

def transaction1(arr):
    n = len(arr)
    if n < 2:
        return 0
    buy = 0
    sell = 1
    max_profit = 0
    while sell < n:
        if arr[sell] > arr[buy]:
            profit = arr[sell]- arr[buy ]
            max_profit = max(max_profit,profit)
        else:
            buy = sell
        sell+=1
    return max_profit


arr =     [7, 10, 1, 3, 6, 9, 2]                   
print (transaction(arr))
print(transaction1(arr))