class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)} \n"
        elif species == 'fish':
            result += f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)} \n"
        elif species == 'bird':
            result += f"Birds in {self.name_of_zoo}: {', '.join(self.birds)} \n"

        result += f'Total animals: {self.__animals}'
        return result


name_zoo = input()
n = int(input())

zoo = Zoo(name_zoo)

for _ in range(n):
    species, type_animal = input().split()
    zoo.add_animal(species, type_animal)

filter_animal = input()

print(zoo.get_info(filter_animal))
