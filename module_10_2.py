"""
Домашнее задание по теме "Потоки на классах"
Цель: научиться создавать классы наследованные от класса Thread.
Задача: "За честь и отвагу!
"""
from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        i = 1
        print(f'{self.name}, на нас напали!')
        for step in range(100-self.power, 0, -self.power):  # снова заглушка - 100-self.power! хз как условие выставить
            print(f'{self.name} сражается {i}день(дня)..., осталось {step} воинов противника.')
            i += 1
            sleep(1)
        print(f'{self.name} одержал победу спустя {i} дней(дня)!')


#  создаем два объекта класса рыцарь
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

#  запускаем потоки в виде класса
first_knight.start()
second_knight.start()

# ждем завершения выполнения потоков
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
