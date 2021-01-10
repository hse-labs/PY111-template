import unittest
import networkx as nx
from typing import Mapping, Hashable

from Tasks.e2_dijkstra import dijkstra_algo


class MyTestCase(unittest.TestCase):
    @staticmethod
    def dict_equal(a: Mapping[Hashable, int], b: Mapping[Hashable, int]):
        for k in a.keys():
            if a[k] != b[k]:
                return False
        return len(a.keys()) == len(b.keys())

    @classmethod
    def setUpClass(cls):
        cls.G = nx.DiGraph()
        cls.G.add_nodes_from("ABCDEFG")
        cls.G.add_weighted_edges_from([
            ("A", "B", 1),
            ("B", "C", 3),
            ("C", "E", 4),
            ("E", "F", 3),
            ("B", "E", 8),
            ("C", "D", 1),
            ("D", "E", 2),
            ("B", "D", 2),
            ("G", "D", 1),
            ("D", "A", 2),
        ])

    def test_first(self):
        self.assertTrue(
            self.dict_equal(
                dijkstra_algo(self.G, 'A'),
                {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 5, 'F': 8, 'G': float("inf")}
            ),
            msg="Результаты неверны. Проверьте реализацию и возвращаемое значение для недостижимых нод (float('inf'))."
        )

    def test_second(self):
        self.assertTrue(
            self.dict_equal(
                dijkstra_algo(self.G, 'D'),
                {'A': 2, 'B': 3, 'C': 6, 'D': 0, 'E': 2, 'F': 5, 'G': float('inf')}
            ),
            msg="Результаты неверны. Проверьте реализацию и возвращаемое значение для недостижимых нод (float('inf'))."
        )

    def test_third(self):
        self.assertTrue(
            self.dict_equal(
                dijkstra_algo(self.G, 'G'),
                {'A': 3, 'B': 4, 'C': 7, 'D': 1, 'E': 3, 'F': 6, 'G': 0}
            ),
            msg="Результаты неверны. Проверьте реализацию и возвращаемое значение для недостижимых нод (float('inf'))."
        )


if __name__ == '__main__':
    unittest.main()
