# Power of numbers

def solution1(n):
    s = str(n)
    rev = int(s[::-1])
    return n ** rev

class Solution:
    # Function to reverse the digits of the number
    def reverse_number(self, n):
        reversed_num = 0
        while n > 0:
            reversed_num = reversed_num * 10 + n % 10
            n //= 10
        return reversed_num

    # Recursive function to compute base raised to the power of exponent
    def reverse_exponentiation_helper(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1

        if exponent % 2 == 0:
            result = self.reverse_exponentiation_helper(base, exponent // 2)
            return result * result
        else:
            result = self.reverse_exponentiation_helper(base, exponent - 1)
            return base * result

    # Main function to compute n raised to the power of its reverse
    def reverse_exponentiation(self, n):
        reversed_num = self.reverse_number(n)
        return self.reverse_exponentiation_helper(n, reversed_num)
