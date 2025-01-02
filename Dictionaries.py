# Dictionaries

dict1 = {
    "Name" : "John",
    "Age" : 24,
    "Sex" : "Male",
    "Loc" : "USA"
}

print(dict1)

#---------------------------------------------------------------------------------------------------------------------#
# Adding Dictionary items and keys
dict1 = { 1:4, 2:16, 3:24 }
dict1[4] = 36
print(dict1)

dict1.update({5:40,6:48})
dict1.update([(7,44),(8,52)])
print(dict1)

d = {1: 10, 2: 20, 3: 30}
for i in range(4, 6):  # Add keys dynamically
    d[i] = i * 10  # Assign a value based on the key
print(d)
print()
#--------------------------------------------------------------------------------------------------------------#
# Accessing values in the dicionary
dict = {}
for i in range(1,11):
    dict[i] = i*i

print(dict.get(5))
print(dict[8])
dlist = list(dict.values())
print(dlist)

#--------------------------------------------------------------------------------------------------------------#
# Accessing Keys in the dictionary
dict = {}
for i in range(1,11):
    dict[i] = i*i

dlist = dict.keys()
print(dlist)
print(list(dlist))

for key in dict:
    print(key,end=", ")

print()
#--------------------------------------------------------------------------------------------------------------#
# Accessing both keys and values in dictionary
dict = {}
for i in range(1,11):
    dict[i] = i*i

dlist = dict.items()
print(dlist)
print(list(dlist))

for key, value in dict.items():
    print(f'Key : {key} --> Value : {value}')

for key in dict:
    print(f'Key : {key} --> Value : {dict[key]}')
print()

#--------------------------------------------------------------------------------------------------------------#
# Removing items from the dictionary
dict = {}
for i in range(1,11):
    dict[i] = i*i

val = dict.pop(4)
dict.popitem()
dict.popitem()
print(val)
print(dict)


