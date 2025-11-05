# Rearrange elements by sign
from Python_Version_I.Stacks_Queues.Prefix_to_Postfix import postfix


def solution1(arr):
    positive = [i for i in arr if i >= 0]
    negative = [i for i in arr if i < 0]
    for i in range(len(positive)):
        arr[2*i] = positive[i]
    for i in range(len(negative)):
        arr[2*i+1] = negative[i]

    return arr

def solution2(arr):
    n = len(arr)
    result = [0]*n
    positive = 0
    negative = 1
    for i in range(n):
        if arr[i] < 0:
            result[negative] = arr[i]
            negative += 2
        else:
            result[positive] = arr[i]
            positive += 2

    return result