import unittest
import numpy as np
import networkx as nx
from Tasks.linear_search import min_search, min_weight_search


class MyTestCase(unittest.TestCase):

	def test_min(self):
		arr = [i for i in range(10)]
		self.assertEqual(min_search(arr), min(arr), "Minimal element is wrong, right answer: " + str(min(arr)))

		arr = [i for i in range(10, -3, -1)]
		self.assertEqual(min_search(arr), min(arr), "Minimal element is wrong, right answer: " + str(min(arr)))

		arr = np.random.rand(1, 300).tolist()
		self.assertEqual(min_search(arr), min(arr), "Minimal element is wrong, right answer: " + str(min(arr)))

	def test_min_weight(self):
		g = nx.Graph()

		nodes = list("ABCDEFGH")
		g.add_nodes_from(nodes)

		edges = [
			('A', 'B', 1),
			('A', 'C', 17),
			('A', 'D', -3),
			('A', 'E', 14),
			('A', 'F', 2),
			('B', 'C', 99),
			('B', 'E', 132),
			('C', 'D', 21),
			('C', 'F', 331),
			('E', 'D', 14),
			('E', 'F', -36),
			('G', 'F', -36),
			('H', 'F', -36),
			('G', 'H', -35.9999999)
		]

		g.add_weighted_edges_from(edges)

		answer = [('E', 'F'), ('F', 'G'), ('F', 'H')]
		self.assertIn(sorted(min_weight_search(g)), answer, "Answer should be one of {}".format(answer))


if __name__ == '__main__':
	unittest.main()
