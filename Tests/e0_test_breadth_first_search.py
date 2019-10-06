import unittest
import networkx as nx
import Tasks.e0_breadth_first_search as bfs


class MyTestCase(unittest.TestCase):
	def test_bfs(self):
		graph = nx.Graph()
		graph.add_nodes_from("ABCDEFGHIJ")
		graph.add_edges_from([
			('A', 'B'),
			('A', 'F'),
			('B', 'G'),
			('F', 'G'),
			('G', 'C'),
			('G', 'H'),
			('G', 'I'),
			('C', 'H'),
			('I', 'H'),
			('H', 'D'),
			('H', 'E'),
			('H', 'J'),
			('E', 'D'),
		])
		result = bfs.bfs(graph, 'A')
		self.assertEqual(
			10,
			len(result),
			msg="Проверьте возвращаемый список - в него либо затесались лишние элементы, либо не хватает элементов."
		)

		result = \
			[result[0]] \
			+ sorted(result[1:3]) \
			+ [result[3]] \
			+ sorted(result[4:7]) \
			+ sorted(result[7:])

		self.assertEqual(
			list("ABFGCHIDEJ"),
			result,
			msg="Возвращаемый список несоответствует нужному порядку обхода."
		)


if __name__ == '__main__':
	unittest.main()
