import unittest
import random

import Tasks.g2_quick_sort as sorter


class MyTestCase(unittest.TestCase):
	def test_sorted(self):
		arr = [random.randint(-100, 100) for _ in range(30)]
		self.assertEqual(
			sorted(arr),
			sorter.sort(arr)
		)


if __name__ == '__main__':
	unittest.main()
