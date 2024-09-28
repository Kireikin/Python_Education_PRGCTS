"""
Домашнее задание по теме "Генераторы"
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
"""
import itertools


def all_variants(text):
    subsequences = []
    for num in range(1, len(text) + 1):
        subsequences.append(list(itertools.combinations(text, num)))  # вычисляем и запоминаем все возможные комбинации
    for subnum in subsequences:
        for deep in subnum:
            subsequences_out = (''.join(deep))  # собираем полученные списки комбинаций в строку
            yield subsequences_out


# Пример работы функции:
if __name__ == '__main__':
    a = all_variants('abc')
    for i in a:
        print(i)
