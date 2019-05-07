import unittest
from Tasks.h0_KMP import kmp_algo


class MyTestCase(unittest.TestCase):

	def test_begin(self):
		haystack = "Hello, tiny world!"
		needle = "Hell"
		self.assertEqual(0, kmp_algo(haystack, needle), "Right index is 0")

	def test_end(self):
		haystack = "All these moments will be lost in time..."
		needle = "time..."
		self.assertEqual(34, kmp_algo(haystack, needle), "'time...' is in the end")

	def test_middle(self):
		haystack = "Шел я лесом, вижу мост, на мосту ворона сохнет. " \
				   "Взял ее за хвост, положил под мост, пускай ворона мокнет."
		needle = "Взял"
		self.assertEqual(haystack.index(needle), kmp_algo(haystack, needle), "Не взяли ворону, ворона вся и высохла.")

	def test_missing(self):
		haystack = "Because only a ginger can call another ginger ginger!"
		needle = "afroamerican"
		self.assertIsNone(kmp_algo(haystack, needle), "Фи, как некультурно, песня о рыжих вообще-то.")


if __name__ == '__main__':
	unittest.main()
