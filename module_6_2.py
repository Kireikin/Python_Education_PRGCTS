class Vehicle:
    owner = str('')
    __model = str('')
    __engine_power = int()
    __color = str()
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    #  __COLOR_VARIANTS = ['Белый', 'Черный', 'Металик волна','Вишня', 'Серый', 'Мокрый асфальт']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self,):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.casefold() in self._Vehicle__COLOR_VARIANTS:
            self._Vehicle__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


# Тестовое задание:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
