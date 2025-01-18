# Permutations 

def permutations(n):
    if n==2 or n==3:
        return -1
    elif n==1:
        return 1
    else:
        evens = []
        odd = []
        for i in range(1,n+1):
            if i%2==0:
                evens.append(i)
            else:
                odd.append(i)
    result =evens+odd
    return result

n =int(input())
result =  permutations(n)
if result==-1:
    print("NO SOLUTION")
elif result == 1:
    print (1)
else:
    print (" ".join(map(str,result)))