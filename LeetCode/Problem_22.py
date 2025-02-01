# Generate Parentheses

def generate1(n,open,close,s, ans):
    if open == n and close == n:
        ans.append(s)
        return
    
    if open < n:
        generate1(n, open+1, close, s+'(', ans)
    if close < open:
        generate1(n, open, close+1, s+')', ans)

def generate(n):
    if n == 0:
        return []
    ans = []
    generate1(n, 0, 0, '', ans)
    return ans

n = 3
print(generate(n))