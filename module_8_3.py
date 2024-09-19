"""
"Создание исключений".
"""


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, reg_nom):
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(reg_nom):
            self.model = model
            self.__vin = vin
            self.__reg_nom = reg_nom

    @staticmethod
    def __is_valid_vin(vin):
        if isinstance(vin, int) and (1000000 <= vin <= 9999999):
            return True
        elif not isinstance(vin, int):
            raise IncorrectVinNumber(f'Некорректный тип vin номер - {vin}')
        elif not (1000000 <= vin <= 9999999):
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера - {vin}')

    @staticmethod
    def __is_valid_numbers(reg_nom):
        if isinstance(reg_nom, str) and len(reg_nom) == 6:
            return True
        elif not isinstance(reg_nom, int):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров - {type(reg_nom)}')
        elif not len(reg_nom) == 6:
            raise IncorrectCarNumbers(f'Неверная длина номера - {len(reg_nom)}')


if __name__ == "__main__":
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
