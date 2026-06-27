class parrot :
    species = "bird"
    def __init__ (self , name , age):
        self.name = name
        self.age = age

ob = parrot("rio", 2)
ob1 = parrot("tio", 3)
print("rio is a {}".format(ob.species))
print("tio also a {}".format(ob1.species))

print("{} is {} years old".format(ob.name,ob.age))
print("{} is {} years old".format(ob1.name , ob1.age))        