# Check if the given number is palindrome or not

def solution1(n):
    rev = 0
    num = n
    while num > 0:
        temp = num % 10
        rev  = rev * 10 + temp
        num //= 10

    if rev == n:
        return "Palindrome"
    else:
        return "False"
    
def solution2(n):
    s = str(n)
    return s == s[::-1]

    
n = 1211111
print(solution2(n))