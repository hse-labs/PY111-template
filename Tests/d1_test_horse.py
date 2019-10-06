import unittest
import Tasks.d1_horse as horse


class MyTestCase(unittest.TestCase):
	def test_1(self):
		self.assertEqual(1152, horse.calculate_paths((8, 8), (7, 7)),
						 msg="Something gonna wrong...")

	def test_2(self):
		self.assertEqual(4608, horse.calculate_paths((9, 9), (8, 8)),
						 msg="Just because...")

	def test_3(self):
		self.assertEqual(830654464, horse.calculate_paths((17, 12), (16, 9)),
						 msg="Oo")

	def test_4(self):
		self.assertEqual(191488, horse.calculate_paths((12, 10), (11, 9)),
						 msg=":)")


if __name__ == '__main__':
	unittest.main()
