# demo class

class dog:
    species = 'Canine'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    
dog1 = dog("Max",12)
dog2 = dog("Maxine",10)

print(dog1.species)
print(dog2.species)
print(dog1.age)
print(dog1.name)
print(dog2.age)
