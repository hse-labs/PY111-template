import unittest
import numpy as np
import networkx as nx
from Tasks.b0_linear_search import min_search, min_weight_search


class MyTestCase(unittest.TestCase):

	def test_min(self):
		arr = [i for i in range(10)]
		self.assertEqual(min_search(arr), min(arr), "Minimal element is wrong, right answer: " + str(min(arr)))

		arr = [i for i in range(10, -3, -1)]
		self.assertEqual(min_search(arr), min(arr), "Minimal element is wrong, right answer: " + str(min(arr)))

		arr = np.random.rand(1, 300).tolist()
		self.assertEqual(min_search(arr), min(arr), "Minimal element is wrong, right answer: " + str(min(arr)))

if __name__ == '__main__':
	unittest.main()
