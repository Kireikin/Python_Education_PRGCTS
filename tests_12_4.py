import logging
from rt_with_exceptions import Runner, Tournament
import unittest


class RunnerTest(Runner):
    
    def __init__(self):
        super().__init__(Runner)

    def test_walk(self):
        try:
            Runner.walk(self)
            logging.info('"test_walk" выполнен успешно')
            return
        except ValueError:
            logging.warning("Неверная скорость для Runner")
            return

    def test_run(self):
        try:
            Runner.run(self)
            logging.info('"test_run" выполнен успешно')
            return
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
            return


if __name__ == "__main__":
    logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='UTF-8',
                        format="%(asctime)s - %(module)s - %(levelname)s  %(funcName)s: - %(lineno)d - %(message)s")

    runner_test = Runner('Петя', -2)
    runner_test2 = Runner(12, 2)
    t = Tournament(101, runner_test, runner_test2)
    print(t.start())

    unittest.main()
