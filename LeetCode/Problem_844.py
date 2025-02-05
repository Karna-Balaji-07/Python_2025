# Backspace string compare

def backspace(s):
    stack = []
    for i in s:
        if i == '#':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return stack

def solution(s1,s2):
    s1 = backspace(s1)
    s2 = backspace(s2)
    s1 = "".join(s1)
    s2 = "".join(s2)
    if s1 == s2:
        return True
    return False

print(solution( "a##c","#a#c"))
