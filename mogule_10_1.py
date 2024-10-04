"""
Домашнее задание по теме "Создание потоков".
Цель: понять как работают потоки на практике, решив задачу
"""
from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            message = ('Какое-то слово №' + str(i+1))
            file.write(message + ' \n')
            sleep(0.1)
    print('Завершилась запись в файл', file_name)


#  выполение функций- потоков последовательно
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print('Работа потоков', time_res)
#  определение потоков
thr_fifth = Thread(target=write_words(10, 'example5.txt'))
thr_sixth = Thread(target=write_words(30, 'example6.txt'))
trh_seven = Thread(target=write_words(200, 'example7.txt'))
thr_eighth = Thread(target=write_words(100, 'example8.txt'))
#  запуск потоков
time_start = datetime.now()
thr_fifth.start()
thr_sixth.start()
trh_seven.start()
thr_eighth.start()
#  ловушка завершения работы потоков
thr_fifth.join()
thr_sixth.join()
trh_seven.join()
thr_eighth.join()
time_end = datetime.now()

time_res = time_end - time_start
print('Работа потоков', time_res)
