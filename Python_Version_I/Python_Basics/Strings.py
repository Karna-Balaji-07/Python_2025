# strings

s1 = "Geeks"
s2 = "for"
s3 = "geeks"
s4 = """ Hello how are you doing
fine very well thank you"""
print(s1,s2,s3,s4,sep="\n")
#----------------------------------------------------------------------------------------------------------#

s5 = "Lovely professional University"
print(s5[0])
print(s5[5])
print(s5[10])
print(s5[-1])
print(s5[-5])

print(s5[1:12])
# to retrive all the characters before or after the specified position
print(s5[:8]) 
print(s5[10:])
# To get the reverse of the string
print(s5[::-1])
# To get characeters at regular intervals
#print(s5[1,20,3])
# negative index slicing
print(s5[-1:-15])
print(s5[-5:])
print(s5[:-6])
print(len(s5))

#----------------------------------------------------------------------------------------------------------#

# Reverse a String
s = "GeeksforGEEKS"
# slicing
print(s[::-1])
# Using reversed and join method
s1 = "".join(reversed(s))
print(s1)
# using loops
s = "Welcome"
rev = ""
for i in s:
    rev = i + rev
print(rev)

# string concatenation
s1 = "Hello "
s2 = "to the "
s3 = "World."
#----------------------------------------------------------------------------------------------------------#
# using + operator
print(s1+s2+s3)
# using .join() method
a = ["Python", "is", "a", "popular", "language", "for", "programming"]
sf = " ".join(a)
print(sf)
# using format() method
res = "Welcome and {} {} {}".format(s1,s2,s3)
print(res)
# using f-strings
print(f'Welcome to the {s3}')

#----------------------------------------------------------------------------------------------------------#

# String formatting using format() method and f-strings
s1 = "Lovely"
s2 = "Professional"
s3 = 3.141923568
res1 = "This is {} {} university".format(s1,s2)
res2 = "Round off {0:1.2f}".format(s3)
print(res1,res2,sep="\n")
print(f' THis is {s1} {s2} university and the value of pi is {s3:{2}.{3}}')
print()

#----------------------------------------------------------------------------------------------------------#

# string methods

s = "Cricket and Football"
s1 = "         Hell0         "
s2 = "           World "
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s.count("t"))
print(s.startswith("C"))
print(s.endswith("L"))
print(s.find("o"))
print(s.index("o"))
print(s.isalnum())
print(s.isalpha())
print(s.isdecimal())
print(s.isdigit())
print(s1.strip())
print(s2.rstrip())


# To sort a string

s = "HelloWorld"
res = sorted(s)
print(res)
s = "".join(res)
print(s)