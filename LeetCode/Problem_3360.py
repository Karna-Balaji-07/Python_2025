# Stone removal game

'''
16
alice 16 - 10 = 6
mark = 6 < 9 : alice wins

alice = 2
alice lose

24
alice 10-24 = 14
mark = 14-9 = 5
alice = 5-8 < 0
alice loses

29
alice 29-10 = 19
mark = 19-9 = 10
alice 10-8 2
mark = 2-7 alice wins

 
'''

def stone(n):
    i = 10
    k = 0
    while n >= i:
        n -= i
        i -= 1
        k += 1
    return k % 2 == 1

        
            

n = 17
print(stone(n))
        