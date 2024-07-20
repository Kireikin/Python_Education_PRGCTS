first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
third = int(input('Введите третье число:'))
if (int(first / second) == 1) and (int(second / third) == 1):  # условие если все равны
    print('Одинаковых чисел :', 3)
elif (int(first / second) == 1) or (int(second / third) == 1) or (int(first / third) == 1):  # условие если два равны
    print('Одинаковых чисел :', 2)
else:
    print('Одинаковых чисел :', 0)
