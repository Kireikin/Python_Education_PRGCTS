"""
Задание по теме "Файлы в операционной системе".
"""
import os
import time

# Материал из лекции:
# print('Текущая директория:', os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')
# print('Текущая директория:', os.getcwd())
# os.makedirs(r'third\fourth')  # создает древо каталогов
# print(os.listdir())  # видим только содержимое активной папки!!! вложенные данные не видны!
# for i in os.walk('.'):
#     print(i)
# os.chdir(r'E:\Python_Education_PRGCTS\module_7') # переход в директорию и активация её текущей
# file = [f for f in os.listdir() if os.path.isfile(f)]  # генерируем список файлов в текущей директории
# dirs = [d for d in os.listdir() if os.path.isdir(d)]  # генерируем список папок в текущей директории
# ('.' - текущая директория)
#  os.system('путь к файлу') - выполнить файл в системе, или команду внешней ос

# Задание ?
directory = '.' 
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.getcwd()
        filetime = os.stat(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.abspath(os.path.join(filepath, os.pardir))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
