class Car:
    def __init__(self, model, vin, reg_nom):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__reg_nom = reg_nom if self.__is_valid_numbers(reg_nom) else None

    def __is_valid_vin(self, vin):
        if isinstance(vin, int) and (1000000<= vin<= 9999999):
            return True
        elif not isinstance(vin, int):
            return IncorrectVinNumber  # 'Некорректный тип {vin} номер'
        elif not (1000000<= vin<= 9999999):
            return IncorrectVinNumber #  'Неверный диапазон для {vin} номера'

    def __is_valid_numbers(self, reg_nom):
        if isinstance(reg_nom, str) and (len(reg_nom) == 6):
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info



class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info



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