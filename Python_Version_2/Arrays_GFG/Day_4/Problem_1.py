# Stock  : Buy and Sell >> Maximum One transaction Allowed.

def solution1(prices):
    res = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            res = max(res, prices[j]- prices[i])
    return res

def solution2(prices):
    mini = prices[0]
    res = 0
    for i in range(1,len(prices)):
        mini = min(mini, prices[i])
        res = max(res, prices[i]-mini)
    return res

arr = [7,10,1,3,6,9,2]
print(solution2(arr))