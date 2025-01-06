# Functions 

def addition():
    print(10+20)
    print("Function")

addition()

# Parameters

def add(a,b):
    print(a+b)

add(3,5)

def details(name,age,sex):
    print(f'My name is {name} and I am {age} years old')
    print(f'I am {sex}')

details("John",20,"Male")

def details1(Name, age, location,occupation):
    print(f'{Name} is {age} years old and is working as {occupation} in {location}')

details1(Name="John Wick", location="New York",occupation="Communicado",age=33)

# variable length arguments

def fun1(*args):
    for i in args:
        print(i,end=" ")
fun1("Hello","Good Morning","Good Evening","Good night","GOod day","Raining")

def fun2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} --> {value} ')
fun2(s1="123",s2="helo",s3="sell",s4="old",s5="new")
print()

# returning multiple values as tuples
def fun3(a,b,c,d):
    sums= a+b
    dif = c-b
    prod = a*d
    div =  prod / dif
    return sums,dif,prod,div

result = fun3(10,20,30,40)
print(result,end="\n")

# returning multiple values as list
def fun4(a,b,c,d):
    sums= a+b
    dif = c-b
    prod = a*d
    div =  prod / dif
    return [sums,dif,prod,div]
result2 = fun4(20,24,28,32)
print(result2,end="\n")

# returning multiple values as dictionary
def fun5(a,b,c,d):
    sums = a+d
    diff = c-b
    prod = sums* diff
    div = prod // diff
    dicts = dict()
    dicts["Addition"] = sums
    dicts["Difference"] = diff
    dicts["Product"] = prod
    dicts["Division"] = div
    return dicts
result3 = fun5(100,250,500,750)
print(result3,end="\n")


# Recursive function example - Factorial

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

result = fact(5)
print(result)

# Recursive function Types
# Tail recursive function
def fact1(n,acc=1):
    if n == 0:
        return acc
    return fact(n,acc*n)

# Non-tail recursive function
def fact2(n):
    if n==1:
        return 1
    return n * fact(n-1)
