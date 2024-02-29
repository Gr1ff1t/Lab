class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print(f"{animal.name} is not in the zoo.")

zoo = Zoo()

lion = Animal("Lion", "Simba")
elephant = Animal("Elephant", "Dumbo")

zoo.add_animal(lion)
zoo.add_animal(elephant)

zoo.remove_animal(lion)

print("Animals in the zoo:")
for animal in zoo.animals:
    print(f"{animal.name} ({animal.species})")