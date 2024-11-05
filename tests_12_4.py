import logging
from rt_with_exceptions import Runner, Tournament
import unittest

logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='UTF-8',
                    format="%(asctime)s - %(module)s - %(levelname)s  %(funcName)s: - %(lineno)d - %(message)s")


class RunnerTest(unittest.TestCase, Runner, Tournament):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner_test = Runner('Петя', -2)
            for i in range(10):
                runner_test.walk()
            self.assertEqual(runner_test.distance, 50)
            return
        except ValueError:
            logging.warning("Неверная скорость для Runner")
            return

    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            runner_test2 = Runner(12, 2)
            for i in range(10):
                runner_test2.walk()
            self.assertEqual(runner_test2.distance, 50)
            return
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
            return


if __name__ == "__main__":
    # first = Runner('Вося', 10)
    # second = Runner('Илья', 5)
    # third = Runner('Арсен', 10)
    # #
    # t = Tournament(101, first, second, third)
    # print(t.start())

    unittest.main()
