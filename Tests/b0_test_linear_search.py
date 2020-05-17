import unittest
import random
from Tasks.b0_linear_search import min_search


class MyTestCase(unittest.TestCase):
    errstr = "Index of minimal element is wrong, right answer: "

    def check_min(self, arr):
        min_index = arr.index(min(arr))
        self.assertEqual(
            min_index,
            min_search(arr),
            self.errstr + str(min_index))

    def test_min(self):
        arr = [i for i in range(3, 10)] + [1]
        self.check_min(arr)

    def test_min_again(self):
        arr = [i for i in range(10, -3, -1)]
        self.check_min(arr)

    def test_min_one_more(self):
        arr = [random.randint(-100, 100) for _ in range(300)]
        self.check_min(arr)


if __name__ == '__main__':
    unittest.main()
