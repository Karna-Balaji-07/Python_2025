# Check whether a number is even or odd

def solution1(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def solution2(n):
    if n  & 1 == 0:
        return "Even"
    return "Odd"



    
n = int(input())
print(solution2(n))
