from typing import Any
import networkx as nx
import matplotlib.pyplot as plt


def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	visited, queue = [], [start_node]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			queue.extend(list(G[vertex]))

	return visited

G = nx.Graph()
# nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# edges = [('A', 'B'), ('A', 'F'), ('B', 'G'), ('F', 'G'), ('G', 'I'), ('G', 'H'), ('G', 'C'), ('H', 'D'), ('H', 'J'),
# 		 ('H', 'D'), ('H', 'E'), ("H", "C"), ("H", "I"), ("D", "E")]
# G.add_node("ABSCDEGHIJ")
# edges = [('A', 'C'), ('A', 'B'), ('C', 'F'), ('B', 'D'), ('B', 'E'), ('E', 'F') ]
G.add_nodes_from("ABCDEFGHIJ")
G.add_edges_from([
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

# nx.draw(G, with_labels=True)
# plt.show()

print(bfs(G, 'A'))
