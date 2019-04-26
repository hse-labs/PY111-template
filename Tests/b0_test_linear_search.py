import unittest
import random
from Tasks.b0_linear_search import min_search


class MyTestCase(unittest.TestCase):

	def test_min(self):
		arr = [i for i in range(1, 10)]
		self.assertEqual(min_search(arr), 0, "Minimal element is wrong, right answer: " + str(min(arr)))

	def test_min_again(self):
		arr = [i for i in range(10, -3, -1)]
		self.assertEqual(min_search(arr), 12, "Minimal element is wrong, right answer: " + str(min(arr)))

	def test_min_one_more(self):
		arr = [random.randint(-100, 100) for _ in range(300)]
		self.assertEqual(min_search(arr), arr.index(min(arr)), "Minimal element is wrong, right answer: " + str(min(arr)))


if __name__ == '__main__':
	unittest.main()
