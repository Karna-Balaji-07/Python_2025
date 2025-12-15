# Minimum removal for target sum

def solution1(arr,k):
    total = sum(arr)
    if total == k:
        return len(arr)
    target = total - k
    dicts = {}
    prefix = 0
    maxlen = -1
    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == target:
            maxlen = i+1
        elif prefix - target in dicts:
            maxlen = max(maxlen, i - dicts[prefix-target])
        if prefix not in dicts:
            dicts[prefix] = i

    return -1 if maxlen == -1 else len(arr)-maxlen


def solution2(arr,k):
    total = sum(arr)
    n = len(arr)
    target = total - k
    if target == 0:
        return n
    left = 0
    curr = 0
    maxlen = -1
    for right in range(n):
        curr += arr[right]
        while left < right and curr > target:
            curr -= arr[left]
            left += 1
        if curr == target:
            maxlen = max(maxlen, right-left+1)

    return -1  if maxlen == -1 else n - maxlen