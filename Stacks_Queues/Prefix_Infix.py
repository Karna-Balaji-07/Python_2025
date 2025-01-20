# Prefix to Infix conversion

def isOperator(c):
    if c=='*' or c=='+' or c=='-' or c=='/' or c=='^' or c==')' or c=='(':
        return True
    return False

def infix(s):
    stack = []
    i = len(s)-1
    while i>=0:
        if not isOperator(s[i]):
            stack.append(s[i])
            i-=1
        else:
            str = "("+stack.pop()+s[i]+stack.pop()+")"
            stack.append(str)
            i-=1
    return stack.pop()

str = "*-A/BC-/AKL" 
print (infix(str))