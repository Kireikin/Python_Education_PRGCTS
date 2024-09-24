"""
"Создание функций на лету"
"""
# Lambda-функция:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
#
# result = list(map(lambda x, y: x == y, first, second))
# """
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.
# """
# print(result)

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        write()

    return write_everything(*data_set)


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])