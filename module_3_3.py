def print_params(a=1, b='Cтрока', c=True):
    print(a, b, c)
    return


#  example 1 - func with def definition
print_params()  # default definitions
print_params(b=str(25))  # работает прямая передача для параметра "b", но параметр д/б srt
print_params(c=[1, 2, 3])  # работает прямая передача для параметра "c", но параметр д/б логической переменной
print()  # zero line
#  example 2 - repackage parameters
values_list = [25, 'Слово', False]
values_dict = {'a': 10, 'b': 'о полку', 'c': True}
print_params(*values_list)
print_params(**values_dict)
print()  # zero line
#  example 3 - repackage with personal parameters
values_list_2 = [54.32, 'Игореве']
print_params(*values_list_2, 42)
print()


# rule for list type
def append_to_list(item, list_my=None):
    if list_my is None:
        # list_my = []
        #  list_my.append(item)
        list_my = [item]  # предложенное упрощение вышеуказанных строк
    print(*list_my)  # если использовать оператор распаковки *, то вывод элементов будет без скобок


append_to_list(1, [12, 12, 12])
append_to_list(3423, [3, 2, 1])
append_to_list(3423)
