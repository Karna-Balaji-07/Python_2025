# Arithmetic operators

x = 10
y = 20

print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x // y )
print( x % y )
print( x ** y )
print()
#----------------------------------------------------------------------------------------------------------#
# Comparison Operators

v = 43234
d = 54354

print(v < d)
print(v <= d)
print(v > d)
print(v >= d)
print(v == d)
print(v != d)
print()
#=============================================================================================================#

# Logical Operators

a = 30
b = 32
c = 11
print( a > b and c < b)
print( a < b or b > a )
print(not a)
print()
#==============================================================================================================#

# Bitwise operators 
a = 10
b = 4
c = 8
print(a & b)
print(b | c)
print(b ^ c)
print(~a)
print(a >> 1)
print(c << 1)
print()
#===============================================================================================================#

# Assignment Operators

a = 5
b = 3
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a%=b
print(a)
a**=b
print(a)
a %= b
print(a)
print()
#===============================================================================================================#

# Member ship and identity operators

lists = [4,8,12,16,20,24,36]
lista = [3,6,9,12,24,36]
name = "Lovely Professional University"
print(24 in lista and 24 in lists)
print(3 in lists)
print(9 not in lista)
print("L" in name)
print("A" in name)

s = "jackie"
a = "jackie"
b = "Jackie"
print(a is s)
print(s is b)
print(s==a)
print(s==b)