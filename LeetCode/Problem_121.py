# best time to buy and sell stock

def transaction1(arr):
    n=len(arr)
    if n<2:
        return 0
    minimum=arr[0]
    max_profit=0
    for i in range(1,n):
        minimum = min(arr[i],minimum)
        max_profit=max(max_profit,arr[i]-minimum)
    return max_profit

def transaction2(arr):
    n=len(arr)
    if n < 2:
        return 0
    buy=0
    max_profit=0
    sell=1
    while sell < n:
        if arr[sell]>arr[buy]:
            profit=arr[sell]-arr[buy]
            max_profit=max(max_profit,profit)
        else:
            buy = sell
        sell+=1
    return max_profit

def transaction3(arr):
    minimum=arr[0]
    max_profit=arr[0]
    profit=0
    for i in arr:
        if i < minimum:
            minimum= i
            max_profit = i
        elif i  >max_profit:
            max_profit=i
            profit=max(max_profit-minimum,profit)
    return profit


prices = [7,1,5,3,6,4]
print(transaction1(prices))
print(transaction2(prices))
print(transaction3(prices))
