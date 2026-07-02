class Dog:
    animal_type = "Mammal"

    def __init__(self, breed, name):
        
        self.breed = breed
        self.name = name

dog1 = Dog("Labradorr", "Max")
dog2 = Dog("Poodle", "jake")
dog3 = Dog("Pugg", "jace")

print(dog1.name, "is a", dog1.breed, "and a", Dog.animal_type)
print(dog2.name, "is a", dog2.breed, "and a", Dog.animal_type)
print(dog3.name, "is a", dog3.breed, "and a", Dog.animal_type)
