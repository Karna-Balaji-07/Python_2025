# loops 

# for loop
a = [10,20,30,40]
for i in a:
    print(i,end=' ')
print()

# for loop in string
s = "Lovely Professional University"
for i in s:
    print(i,end=",")
print()

# using range() function
for i in range(10):
    print(i,end=" ")
print()

for i in range(1, 12):
    print(i,end=" ")
print()

for i in range(0,20,2):
    print(i,end=" ")
print()

# control statements in loops
for i in range(20):
    if i % 2 == 0:
        continue
    print(i,end=" ")
print()

for i in range(20):
    if i==10:
        break
    print(i,end=" ")
print()

for i in range(20):
    if i % 3 == 0:
        pass
    print(i,end=" ")
print("\n-------------------------------------------------------------\n")
#===================================================================================================================================#

# While loops

count = 0
while count < 10:
    print(count,end=" ")
    count += 1
print()

