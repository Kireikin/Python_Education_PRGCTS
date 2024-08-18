class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):  # код из предыдущего задания
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('"Такого этажа не существует".')
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей:{self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(str(h1))   # доработано, тк в тз не было указано обращение к str
print(str(h2))   # --//--

# __len__
print(len(h1))
print(len(h2))
