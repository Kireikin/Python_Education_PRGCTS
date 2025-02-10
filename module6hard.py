"""
Дополнительное практическое задание по модулю: "Наследование классов.
"""
import math


class Figure:
    def __init__(self, color, sides):
        self.sides_count = None  # (количество сторон)
        self.__sides = self.set_sides(sides)  # (список сторон, целые числа - инкапсулированный)
        self.__color = self.set_color(r=color[0], g=color[1], b=color[2])  # (список цветов в формате RGB - инкапсулированный)
        self.filled = False  # (признак закрашенной фигуры - Boolean)

    def get_color(self):  # возвращает список RGB цветов
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):  # проверяет корректность переданных значений (служебный метод)
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):  # изменяет атрибут __color
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            return [r, g, b]
        else:
            print(f'Введенный цвет {r, g, b} не верен, цвет не поменялся:')

    @staticmethod
    def __is_valid_sides(self, *sides):  # принимает неограниченное кол-во сторон, возвращает True если все стороны
        # целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        if len(sides) == self.sides_count:
            return True
        for side in sides:
            if not isinstance(side, int) or not (side > 0):
                return False

    def get_sides(self):  # должен возвращать значение атрибута __sides.
        return self.__sides

    def __len__(self):  # должен возвращать периметр фигуры.
        if self.sides_count == 1:
            return self.__sides
        else:
            print(self.__sides, 'получено', id(self.__sides))
            print(self.sides_count)
            summa = sum(self.__sides)
            return summa

# ('Метод set_sides(self, *new_sides) - должен принимать новые стороны, если их количество не равно sides_count, то не '
# 'изменять, в противном случае - менять.') - непонятная формулировка задания!!!
    # нужно понимать как :
#  - должен изменить на новые длины сторон(ы) "__sides" если их количество равно sides_count, в противном случае
    #  - не изменять, в дополнении сказано присваивать сторонам единичные значения.
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
            print(f'Длины сторон изменены на {self.__sides}')
            return self.__sides
        else:
            print('Количество сторон не совпали, изменения не приняты')




class Circle(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count: int = 1

    def __radius(self):
        return len(self) / 2 / 3.14

    def get_square(self):
        return self.__radius() * self.__radius() * 3.14 / 2


class Triangle(Figure):
    def __init__(self, color, sides):
        Figure.__init__(self, color, sides)
        self.sides_count: int = 3

    def get_square(self):  # Площадь треугольника по формуле Герона
        p = 0.5 * len(self)
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count: int = 12
        self.__sides = [sides]*12
        print(self.__sides, 'создано бл', id(self.__sides))

    def get_volume(self):  # Обьем куба
        return self.__sides[0] ** 3


# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
# triangle1 = Triangle((200, 200, 100), (5, 6, 7))

# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'Текущий цвет обьекта {circle1.__class__.__name__} - {circle1.get_color()}')
# cube1.set_color(300, 70, 15)  # Не изменится
# print(cube1.get_color())
# triangle1.set_color(100, 100, 100)  # дополнение теста для треугольника
# print(triangle1.get_color())

#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
# print(circle1.get_sides())

# triangle1.set_sides(15, 16, 5)  # дополнение теста для треугольника
# print(triangle1.get_sides())

# cube1.set_sides(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)  # дополнение теста для треугольника
# print(cube1.get_sides())

# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
# print(len(triangle1))  # дополнение теста для треугольника
# print(len(cube1))  # дополнение теста для куба
#

# # Проверка объёма (куба):
# print(cube1.get_volume())
