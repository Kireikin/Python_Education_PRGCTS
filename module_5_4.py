class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args not in cls.houses_history:
            cls.houses_history.append(args)
        else:
            print('Такой дом уже есть')
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


#  Тест:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# h4 = House('ЖК Матрёшки', 20)  # проверка условий в __new__

# Удаление объектов
del h2
del h3

print(House.houses_history)
