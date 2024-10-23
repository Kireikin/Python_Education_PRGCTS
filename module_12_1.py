import runner
import unittest as ut


class RunnerTest(ut.TestCase):
    def test_walk(self):
        runner1 = runner.Runner('Сергей')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = runner.Runner('Григорий')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = runner.Runner('Даша')
        runner4 = runner.Runner('Маша')
        for i in range(10):
            runner3.run()
            runner3.walk()
            runner4.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, 100)
        self.assertNotEqual(runner4.distance, 100)


if __name__ == "__main__":
    ut.main()
