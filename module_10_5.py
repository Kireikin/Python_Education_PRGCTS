"""
Домашнее задание по теме "Многопроцессное программирование"
Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
Задача "Многопроцессное считывание"
"""
from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        all_data.append(file.readlines())
#    return all_data


if __name__ == '__main__':
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# Линейный вызов:
    time_start = datetime.now()
    for filename in file_names:
        read_info(filename)
    time_end = datetime.now()
    time_res = time_end - time_start
    print('Работа линейного чтения', time_res)
    # print(read_info(file_names[0]))

#  Многопроцессный:
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    time_end = datetime.now()
    time_res = time_end - time_start
    print('Многопроцессного чтения', time_res)
