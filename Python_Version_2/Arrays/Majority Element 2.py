# Find the element that occurs more than n//3 times

def solution1(arr):
    n = len(arr)
    ele1 = -1
    ele2 = -1
    cnt1 = 0
    cnt2 = 0

    for i in arr:
        if ele1 == i:
            cnt1 += 1
        elif ele2 == i:
            cnt2 += 1
        elif cnt1 == 0:
            cnt1 += 1
            ele1 = i
        elif cnt2 == 0:
            cnt2 += 1
            ele2 = i
        else:
            cnt1 -= 1
            cnt2 -= 1

    result = []
    count1, count2 = 0,0
    for i in arr:
        if i == ele1:
            count1 += 1
        if i == ele2:
            count2 += 1

    if count1 > n//3:
        result.append(ele1)
    if count2 > n//3 and ele1 != ele2:
        result.append(ele2)

    return result