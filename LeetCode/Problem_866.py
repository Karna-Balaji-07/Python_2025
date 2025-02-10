# Prime Palindrome

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1] 

def next_prime(n):
    while True:
        if is_palindrome(n) and prime(n):
            return n
        n += 1
        if 10**7 < n < 10**8:
            n = 10**8




n = 6
print(next_prime(n))
n = 13
print(next_prime(n))
