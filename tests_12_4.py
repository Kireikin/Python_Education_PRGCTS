import logging
from rt_with_exceptions import Runner, Tournament
import unittest

logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='UTF-8',
                    format="%(asctime)s - %(module)s - %(levelname)s  %(funcName)s: - %(lineno)d - %(message)s")


class RunnerTest(Runner):
    def __init__(self):
        super().__init__(Runner)

    @classmethod
    def setUpClass(cls):
        print('TEST IS STARTED')

    def test_walk(self):
        try:
            runner_test = Runner('Петя', -2)
            runner_test.walk()
            logging.info('"test_walk" выполнен успешно')
            return
        except ValueError:
            logging.warning("Неверная скорость для Runner")
            return

    def test_run(self):
        try:
            runner_test2 = Runner(12, 2)
            runner_test2.run()
            logging.info('"test_run" выполнен успешно')
            return
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
            return

    @classmethod
    def tearDownClass(cls):
        print('TEST IS COMPLETE')


if __name__ == "__main__":
    # first = Runner('Вося', 10)
    # second = Runner('Илья', 5)
    # third = Runner('Арсен', 10)
    #
    # t = Tournament(101, first, second, third)
    # print(t.start())

    unittest.main()
