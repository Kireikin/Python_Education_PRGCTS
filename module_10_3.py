"""
Домашнее задание по теме "Блокировки и обработка ошибок"
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
Задача "Банковские операции":
"""

from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance: int = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            adding_balance = randint(50, 500)
            self.balance += adding_balance
            print(f'Пополнение: {adding_balance}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for j in range(100):
            withdrawing = randint(50, 500)
            print(f'Запрос на {withdrawing}')
            if withdrawing <= self.balance:
                self.balance -= withdrawing
                print(f'Снятие:{withdrawing}. Баланс:{self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


if __name__ == '__main__':
    bk = Bank()
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()
