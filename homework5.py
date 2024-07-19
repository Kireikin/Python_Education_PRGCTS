immutable_var = ('Кортеж', 12345, True, [1, 2, True], [4, 'Text'], [7, False])
print(immutable_var) # выводим кортеж тип 'tuple'
#print(type(immutable_var)) # проверка
# immutable_var[0] = 1  - TypeError: 'tuple' object does not support item assignment
mutable_list = list(immutable_var[3:]) # присваеваем преобразованный в список 'list'
mutable_list[1][1] = "Modified Список"
print(mutable_list)
#print(type(mutable_list)) # проверка
