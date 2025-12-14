# Find the minimum penalty for the shop

def solution(s):
    prefix = [0] * (len(s)+1) # Open and not coming
    suffix = [0] * (len(s)+1) # closed and coming

    for i in range(1,len(s)+1):
        if s[i-1] == 'N':
            prefix[i] = prefix[i-1]+1
        else:
            prefix[i] = prefix[i-1]


    for i in range(len(s)-1,-1,-1):
        if s[i] == 'Y':
            suffix[i] = suffix[i+1] + 1
        else:
            suffix[i] = suffix[i+1]

    penalty = float('inf')
    hour = float('inf')
    for i in range(len(s)):
        curr = prefix[i] + suffix[i]
        if curr < penalty:
            penalty = curr
            hour = i

    return hour, penalty

s = "YYNY"
print(solution(s))