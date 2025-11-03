# 821. shortest distance to a calender

def solution1(s,c):
    arr = []
    index = []
    for i in range(len(s)):
        if s[i] ==c:
            index.append(i)
    

    for i in range(len(s)):
        mini = float('inf')
        for j in index:
            diff = abs(i-j)
            mini = min(mini,diff)
        arr.append(mini)
    return arr

s = "loveleetcode"
c = "e"
print(solution1(s,c))