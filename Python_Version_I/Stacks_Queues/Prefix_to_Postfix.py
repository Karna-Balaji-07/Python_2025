# Prefix to postfix conversion

def isOperator(c):
    if c=='*' or c=='+' or c=='-' or c=='/' or c=='^' or c==')' or c=='(':
        return True
    return False

def postfix(exp):
    stack = []
    i = len(exp)-1
    while i >= 0:
        if not isOperator(exp[i]):
            stack.append(exp[i])
            i -= 1
        else:
            str = stack.pop()+stack.pop()+exp[i]
            stack.append(str)
            i-=1
    return stack.pop()

s = "*-A/BC-/AKL"
print(postfix(s))
