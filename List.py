# Lists

# creating lists

# using []
list1 = [1,2,3,4,5,6]
list2 = [1,1.2,1.3,"Hello"]
# using list() method
s = (1,2,3,4,5)
list3 = list(s)
print(list3)

# list with repeated elements
list4 = [2]*7
list5 = [0] * 2
print(list4, list5,sep="\n")

#----------------------------------------------------------------------------------------------------------#

# Accessing elements in a list
print(list1[0])
print(list2[-1])

#----------------------------------------------------------------------------------------------------------#

# Adding elements into the list
list1.append(7)
list1.append(9)
list2.extend(["World",121,1.42233])
list2.insert(0,1000)
print(list1)
print(list2)
# 

#----------------------------------------------------------------------------------------------------------#

# Removing element from the list
list1.remove(9)
list1.remove(2)
list2.pop()
list2.pop(4)
del list1[2]
print(list1)
print(list2)

#----------------------------------------------------------------------------------------------------------#

# Taking input for a list
#user_input = input().split()
#print(user_input)

l = []
#for i in range(10):
 #   ele = int(input())
  #  l.append(ele)
#print(l)

#user_input = list(map(int,input().split()))
#print(user_input)

#----------------------------------------------------------------------------------------------------------#

# to access both index and value of the list
lists = ["Hello","how","Good","Bad"]
for index,value in enumerate(lists):
    print(index,value,sep=",")

#-----------------------------------------------------------------------------------------------------------#

# Given two lists with elements and indices, WAP to find elements of list1 at indices present in list2
#approach1
def approach1(l1, l2):
    arr = []
    for i in l2:
        arr.append(l1[i])
    print(arr)

l1 =['Hello', 'geeks', 'for', 'geeks']# [10, 20, 30, 40, 50]
l2 = [1,2,3]

def approach2(l1,l2):
    arr = []
    index_map = {index : element for index,element in enumerate(l1)}
    for i in l2:
        arr.append(index_map[i])
    print(arr)

approach1(l1,l2)
approach2(l1,l2)
print()
#--------------------------------------------------------------------------------------------------------#

# Given a list, task is to find a given string in list
def approach21(l1, s):
    counts = l1.count(s)
    if counts >= 1:
        return True
    return False
    
def approach22(l1,s):
    if s in l1:
        return True
    return False



l1 = [1, 2.0, 'have', 'a', 'geeky', 'day']
s = "geeky"
res = approach21(l1,s)
res22 = approach22(l1,s)
print(res)
print(res22)

#--------------------------------------------------------------------------------------------------------#

# Find the indices of a given element in the list

def approach31(l1,element):
    arr = []
    for index,value in enumerate(l1):
        if value == element:
            arr.append(index)
    return arr

def approach32(l1,element):
    arr = []
    for i in range(len(l1)):
        if l1[i] == element:
            arr.append(i)
    return arr

l1 = [1,3,7,2,7,4,7,7]
print(approach31(l1,7))
print(approach32(l1,7))

#--------------------------------------------------------------------------------------------------------#

# Find the most frequent element in the list

def approach41(l1):
    count = 0
    num = l1[0]
    for i in l1:
        freq = l1.count(i)
        if freq > count:
            num = i
    return num

def approach42(l1):
    dict = {}
    count,itm = 0,""
    for i in reversed(l1):
        dict[i] = dict.get(i,0)+1
        if dict[i] > count:
            count,itm = dict[i], i
    return itm


l1 = [2,4,6,2,5,2,8,8,9,3,9,2,2]
print(approach41(l1))
print(approach42(l1))

#--------------------------------------------------------------------------------------------------------#

# Remove multiple elements from the list

def approach51(l1,l2):
    arr = []
    for i in l1:
        if i not in l2:
            arr.append(i)
    return arr

def approach52(l1,l2):
    for i in l2:
        while i in l1:
            l1.remove(i)
    return l1

l1 = [10,20,30,40,50,60,70,80]
l2 = [30,40,60]
print(approach51(l1,l2))
print(approach52(l1,l2))

#--------------------------------------------------------------------------------------------------------#

# concatenate two lists element-wise

def approach61(l1,l2):
    arr = []
    for i in range(len(l1)):
        arr.append(str(l1[i]) + str(l2[i]))
    return arr

l1 = [1,2,3,4]
l2 = ["Hi","Hello","Why","Who"]
print(approach61(l1,l2))