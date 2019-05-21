from typing import Any
import networkx as nx


def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	x = [start_node]
	queue = [start_node]
	tracks = {node: [] for node in g.nodes}
	while queue:
		element = queue.pop(0)
		y = list(g.neighbors(element))
		for node in y:
			if node not in x:
				x.append(node)
				queue.append(node)
				tracks[node].extend((*tracks[element], element))
	return x

