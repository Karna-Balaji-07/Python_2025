# Recursive string problem

def recursion1(s):
    if len(s) == 0:
        return 
    temp = s[0]
    recursion1(s[1:])
    print(temp,end="")

s = "Hello wsorld"
recursion1(s)