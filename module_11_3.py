"""
Домашнее задание по теме "Интроспекция"
Цель задания:
Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.
"""
import inspect
from pprint import pprint


class SomeClassEdu:
    """ Тренировочный класс для отработки задания модуля 11 упр.3 """
    _loc_data = [1, 2, 3, 4, 5, 6, True, False, 'Вектор']

    def __init__(self, param_1, *arg2, **keys):
        self.param_1 = param_1
        self.arg2 = arg2
        self.keys = keys

    def list_data(self):
        """ Выводит значения скрытого атрибута _loc_data """
        print(self.param_1, ' ', self.arg2)

    def some_class_metod(self, value):
        self._loc_data = value
        print(self._loc_data)


def introspection_info(obj):  # процедура/метод проведения интроспекции объекта
    # без библиотеки интроспекции:
    obj_info_out = {'Type': type(obj).__name__, 'Module': inspect.getmodule(obj), 'DOC': inspect.getdoc(obj)}
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        obj_info_out[attr_name] = type(attr).__name__
    if inspect.isclass(obj):
        obj_info_out['fullargspec'] = inspect.getfullargspec(victum.list_data)

    #  с библиотекой:

    return obj_info_out


'''Задание: Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит 
интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
'''
if __name__ == '__main__':
    victum = SomeClassEdu(4, [23, 23, 23, 32], [True, False])
    number_info = introspection_info(42)
    pprint(number_info)

    obj_info = introspection_info(victum)
    pprint(obj_info)

#    help(inspect)
