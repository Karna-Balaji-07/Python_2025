# Repetitions

def repetitions(s):
    count = 0
    maxs =0
    n = len(s)
    i=1
    while i < n:
        if s[i] == s[i-1]:
            count += 1
            maxs = max(count,maxs)
            i+=1
        else:
            i+=1
            count=0
    return maxs+1


        
        

s = input()
print(repetitions(s))