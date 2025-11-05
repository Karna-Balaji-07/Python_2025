# Stock buy and sell

def solution1(arr):
    buy = 0
    sell = 1
    profit = float('-inf')
    while sell < len(arr):
        if arr[buy] < arr[sell]:
            profit = max(profit, arr[sell]-arr[buy])
            sell += 1
        else:
            buy += 1
            sell += 1
            if buy == sell:
                sell += 1

    return profit

def solution2(arr):
    profit = 0
    minprice = float('inf')
    for i in range(len(arr)):
        minprice = min(minprice, arr[i])
        profit = max(profit, arr[i]-minprice)

    return profit


prices = [7,1,5,3,6,4]
print(solution1(prices))
