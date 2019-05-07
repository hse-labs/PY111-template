from typing import Any
import networkx as nx


def dfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	visited, stack = [], [start_node]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.append(vertex)
			stack.extend(g[vertex] )

	return visited

G = nx.Graph()
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

print(dfs(G, 'A'))