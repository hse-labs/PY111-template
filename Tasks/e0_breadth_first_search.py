from typing import Any
import networkx as nx
import matplotlib.pyplot as plt
# import Tasks.a1_my_queue as qu_methods


def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	visited = [start_node]
	queue = [start_node]
	tracks = {node: [] for node in g.nodes}
	while queue:
		element = queue.pop(0)
		neighbors = list(g.neighbors(element))
		for node in neighbors:
			if node not in visited:
				visited.append(node)
				queue.append(node)
				tracks[node].extend((*tracks[element], element))
	print(tracks)
	return visited


if __name__ == '__main__':
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
	result = bfs(graph, 'A')
	nx.draw(graph, with_labels=True)
	plt.show()
	print(result)
