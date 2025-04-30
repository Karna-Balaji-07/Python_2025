print("Hello world")

# Variables
name = "John wick"
age = 234
_wers = 3231

# dynamically typed variables
x = 123
x = "Jphn"
x = 1.23

# Assigned variables in one line
a = b = c = 100
print(a,b,c)
a,b,c = 12,"Jon",2.34
print(a,b,c)

#----------------------------------------------------------------------------------------------------------------------------------#

# Input output

# end() parameter
a = b = c = 100
print(a,b,c,end="-=-\n")
a,b,c = 12,"Jon",2.34
print(a,b,c,end="next\n")

for i in range(10):
    print(i,end=",")
print()
# sep() parameter
a = b = c = 100
print(a,b,c,sep="-")
a,b,c = 12,"Jon",2.34
print(a,b,c,sep="/")

# input
name = input("Name: ")
print(name)

age = int(input("Age: "))
print(age)

grade = float(input("GPA: "))
print(grade)

x,y,z = input().split()
print(x)
print(y)
print(z)


a = [i for i in input().split()]
print(a)

b = [int(i) for i in input().split(',')]
print(b)


a = map(int,input().split())
b = list(a)
print(b)
a = map(int,input().split(","))
b = list(a)
print(b)
print(a)
