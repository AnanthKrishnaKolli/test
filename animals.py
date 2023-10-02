class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        return "Meow!"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.species})")

def main():
    zoo = Zoo()

    fido = Dog("Fido", breed="Golden Retriever")
    mittens = Cat("Mittens", color="Gray")

    zoo.add_animal(fido)
    zoo.add_animal(mittens)

    for animal in zoo.animals:
        sound = animal.make_sound()
        print(f"{animal.name} makes the sound: {sound}")

if __name__ == "__main__":
    main()
