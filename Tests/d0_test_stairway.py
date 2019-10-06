import unittest
import Tasks.d0_stairway as stairway_to_heaven


class MyTestCase(unittest.TestCase):
	def test_1(self):
		test_st = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
		self.assertEqual(26, stairway_to_heaven.stairway_path(test_st),
						 msg="There's a lady who's sure all that glitters is gold")

	def test_2(self):
		test_st = [4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]
		self.assertEqual(19, stairway_to_heaven.stairway_path(test_st),
						 msg="And she's buying a stairway to heaven")

	def test_3(self):
		test_st = [5, 11, 43, 2, 23, 43, 22, 12, 6, 8]
		self.assertEqual(72, stairway_to_heaven.stairway_path(test_st),
						 msg="When she gets there she knows, if the stores are all closed")

	def test_4(self):
		test_st = [4, 12, 32, 22, 1, 7, 0, 12, 4, 2, 2]
		self.assertEqual(41, stairway_to_heaven.stairway_path(test_st),
						 msg="With a word she can get what she came for")


if __name__ == '__main__':
	unittest.main()
