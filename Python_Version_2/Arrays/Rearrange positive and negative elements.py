# rearrange array elements by sign

def solution1(arr):
    pos = []
    neg = []
    for i in arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)

    positive = 0
    negative = 0
    index =0
    while positive < len(pos) and negative < len(neg):
        if index  % 2 == 0:
            arr[index] = pos[positive]
            positive += 1
        else:
            arr[index] = neg[negative]
            negative += 1
        index += 1

    while positive < len(pos):
        arr[index] = pos[positive]
        index += 1
        positive += 1

    while negative < len(neg):
        arr[index]=neg[negative]
        index += 1
        negative += 1

    return arr