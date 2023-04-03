# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, room, population):
        self.population = population
        self.room = room

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.population


person = Person(41, 999)
print(person.get_person_room())
print(person.get_city_population())
