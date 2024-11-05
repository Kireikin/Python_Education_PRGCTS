import logging
from rt_with_exceptions import Runner
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
        except ValueError:
            logging.warning("Неверный тип данных для объекта Runner")
            return


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    runner_test = Runner('Петя', 0)
    runner_test2 = Runner('1234', 2)
    unittest.main()
