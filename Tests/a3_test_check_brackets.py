import unittest
from Tasks.a3_check_brackets import check_brackets


class MyTestCase(unittest.TestCase):
	def test_invalid(self):
		self.assertFalse(check_brackets("(()("))
		self.assertFalse(check_brackets("(()))"))
		self.assertFalse(check_brackets("(()))"))

	def test_valid(self):
		self.assertTrue(check_brackets("(()())"))
		self.assertTrue(check_brackets("((()(())()))()"))


if __name__ == '__main__':
	unittest.main()
