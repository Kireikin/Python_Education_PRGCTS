import unittest
# import module_12_1
import module_12_2


class Test12M3(unittest.TestCase):
    def __init__(self, is_frozen=True):
        super().__init__()
        self.is_frozen = is_frozen

    def test_sprint1(self):
        module_12_2.TournamentTest.test_sprint1()

    # def test_sprint2(self):
    #     test2 = module_12_2.TournamentTest.test_sprint2
    #
    # def test_sprint3(self):
    #     test3 = module_12_2.TournamentTest.test_sprint3


if __name__ == "__main__":
    unittest.main()
