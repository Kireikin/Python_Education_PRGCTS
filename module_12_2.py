import runner_and_tournament as runtour
import unittest as ut
'''Домашнее задание по теме "Методы Юнит-тестирования" Цель: освоить методы, которые содержит класс TestCase. Задача: 
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub 
https://github.com/yanchuki/HumanMoveTest/blob/master/runner_and_tournament.py. (Можно скопировать) В этом коде 
сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament. Изменения в классе Runner: 
Появился атрибут speed для определения скорости бегуна. Метод __eq__ для сравнивания имён бегунов. Переопределены 
методы run и walk, теперь изменение дистанции зависит от скорости. Класс Tournament представляет собой класс 
соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, 
который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех 
тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament 
запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в 
котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего 
бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с
 меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
'''


class TournamentTest(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        print('TEST IS STARTED')

    def setUp(self):
        self.runner_1 = runtour.Runner('Усэйн', 10)
        self.runner_2 = runtour.Runner('Андрей', 9)
        self.runner_3 = runtour.Runner('Ник', 3)

    def test_sprint1(self):
        sprint_1 = runtour.Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results[1] = sprint_1.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[1][2], 'Ник')
        # print('Track run 1')

    def test_sprint2(self):
        sprint_2 = runtour.Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results[2] = sprint_2.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[2][2], 'Ник')
        # print('Track run 2')

    def test_sprint3(self):
        sprint_3 = runtour.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results[3] = sprint_3.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[3][3], 'Ник')
        # print('Track run 3')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for number_test in TournamentTest.all_results:
            print(number_test, ':', end=' ')
            for i in TournamentTest.all_results[number_test]:
                print(i, '-', TournamentTest.all_results[number_test][i], end=' ')
            print()
        print('TEST IS COMPLETE')


if __name__ == "__main__":
    ut.main()
