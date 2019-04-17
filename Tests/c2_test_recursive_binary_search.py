import unittest
from Tasks.c2_recursive_binary_search import binary_search


class MyTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.arr = [i for i in range(100)] + [101]

	def test_existing(self):
		self.assertEqual(binary_search(5, self.arr), 5, msg="Invalid index returned!")
		self.assertEqual(binary_search(54, self.arr), 54, msg="Invalid index returned!")

	def test_missing(self):
		self.assertIsNone(binary_search(-1, self.arr),
						  msg="Answer should be None because element is not presented in the array")
		self.assertIsNone(binary_search(100, self.arr),
						  msg="Answer should be None because element is not presented in the array")

	def test_borders(self):
		self.assertEqual(binary_search(0, self.arr), 0,
						 msg="First element is not found - maybe 'mid - 1' is missing?")
		self.assertEqual(binary_search(101, self.arr), 100,
						 msg="Last element is not found - maybe 'mid + 1' is missing?")


if __name__ == '__main__':
	unittest.main()
