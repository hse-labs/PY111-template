import unittest
from Tasks.c2_recursive_binary_search import binary_search


class MyTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.arr = [i for i in range(100)] + [101]

	def test_existing(self):
		self.assertEqual(5, binary_search(5, self.arr), msg="Invalid index returned!")
		self.assertEqual(54, binary_search(54, self.arr), msg="Invalid index returned!")

	def test_missing(self):
		self.assertIsNone(binary_search(-1, self.arr),
						  msg="Answer should be None because element is not presented in the array")
		self.assertIsNone(binary_search(100, self.arr),
						  msg="Answer should be None because element is not presented in the array")

	def test_borders(self):
		self.assertEqual(0, binary_search(0, self.arr),
						 msg="First element is not found - maybe 'mid - 1' is missing?")
		self.assertEqual(100, binary_search(101, self.arr),
						 msg="Last element is not found - maybe 'mid + 1' is missing?")


if __name__ == '__main__':
	unittest.main()
