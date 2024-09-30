"""
Домашнее задание по теме "Декораторы"
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
"""
from math import sqrt


def is_prime(func):
    def wrapper(*arg):
        original_result = func(*arg)
        prime = True
        i = 2
        while i <= sqrt(original_result):
            if original_result % i == 0:
                prime = False
                break
            i += 1
        if prime:
            print('Простое число')
        else:
            print('Составное число')
        return original_result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
