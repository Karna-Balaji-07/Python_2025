# print all the premutations of the string

from itertools import permutations
def solution1(s):
    return [''.join(p) for p in permutations(s)]

def recursive(s,step=0):
    if step == len(s):
        print(''.join(s))
        return
    
    for i in range(step, len(s)):
        s_list = list(s)
        s_list[step],s_list[i] = s_list[i],s_list[step]

        recursive(s_list,step+1)
a = 'ABC'
print(recursive(a))