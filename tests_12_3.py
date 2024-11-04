import runner
import runner_and_tournament as runtour
import unittest as ut


class RunnerTest(ut.TestCase):
    is_frozen = False

    @ut.skipIf(is_frozen, "'Тесты в этом кейсе заморожены'.")
    def test_walk(self):
        runner1 = runner.Runner('Сергей')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @ut.skipIf(is_frozen, "'Тесты в этом кейсе заморожены'.")
    def test_run(self):
        runner2 = runner.Runner('Григорий')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @ut.skipIf(is_frozen, "'Тесты в этом кейсе заморожены'.")
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


class TournamentTest(ut.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        print('TEST IS STARTED')

    def setUp(self):
        self.runner_1 = runtour.Runner('Усэйн', 10)
        self.runner_2 = runtour.Runner('Андрей', 9)
        self.runner_3 = runtour.Runner('Ник', 3)

    @ut.skipIf(is_frozen, "'Тесты в этом кейсе заморожены'.")
    def test_sprint1(self):
        sprint_1 = runtour.Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results[1] = sprint_1.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[1][2], 'Ник')
        # print('Track run 1')

    @ut.skipIf(is_frozen, "'Тесты в этом кейсе заморожены'.")
    def test_sprint2(self):
        sprint_2 = runtour.Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results[2] = sprint_2.start()
        ut.TestCase.assertEqual(self, TournamentTest.all_results[2][2], 'Ник')
        # print('Track run 2')

    @ut.skipIf(is_frozen, "'Тесты в этом кейсе заморожены'.")
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
