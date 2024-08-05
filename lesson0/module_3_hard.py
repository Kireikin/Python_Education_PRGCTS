def calculate_structure_sum(*data):
    global sum
    for data_ in data:
        if isinstance(data_, int):
            sum += data_
        elif isinstance(data_, str):
            sum += len(data_)
        elif isinstance(data_, (tuple, list, set)):
            for data__ in data_:
                calculate_structure_sum(data__)
        elif isinstance(data_, dict):
            for k, v in data_.items():
                calculate_structure_sum(k)
                calculate_structure_sum(v)
    return sum


sum = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print('Выходные данные (консоль):')
print(result)

# Типы данных:
# print(1, type([1, 2, 3]), isinstance([1, 2, '23'], list), [1, 2, 3])
# print(2, type({'a': 4}), isinstance({'a': 4, 'b': 5}, dict), {'a': 4, 'b': 5})
# print(3, type(((), [{(2, 'Urban', ('Urban2', 35))}])), ((), [{(2, 'Urban', ('Urban2', 35))}]))
# print(4, isinstance(((), [{(2, 'Urban', ('Urban2', 35))}]), tuple))
# print(5, isinstance({(2, 'Urban', ('Urban2', 35))}, set))
