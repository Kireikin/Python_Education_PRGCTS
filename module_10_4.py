"""
Домашнее задание по теме "Очереди для обмена данными между потоками.
Цель: Применить очереди в работе с потоками, используя класс Queue.
Задача "Потоки гостей в кафе"
"""
import queue
from threading import Thread
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:

    def __init__(self, *table):
        self.tables = table
        self.o4eredb = queue.Queue()

    def guest_arrival(self, *guests):  # Должен принимать неограниченное кол-во гостей
        for g in guests:
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    print(f'{t.guest.name} сел(-а) за стол номер {t.number}')
                    t.guest.start()
                    break  # for t # выход из цикла столов для клиента за столом
            else:  # забиваем в очередь
                self.o4eredb.put(g)
                print(f'{g.name} в очереди".')

    def discuss_guests(self):  # Этот метод имитирует процесс обслуживания гостей.
        while (not self.o4eredb.empty()) or (self.tables is None):
            for t in self.tables:
                if t.guest.is_alive():
                    print(f'"{t.guest.name} покушал(-а) и ушёл(ушла)"')
                    print(f'"Стол номер {t.number} свободен".')
                    t.guest = None
                    if not self.o4eredb.empty():
                        t.guest = self.o4eredb.get()
                        print(f'"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}"')
                        t.guest.start()
        else:
            print('Гости покинули кафе')


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
