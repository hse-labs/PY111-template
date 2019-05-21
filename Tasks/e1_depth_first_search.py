from typing import Any
import networkx as nx


def dfs(g: nx.Graph, start_node: Any) -> str:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	x = []
	stack = [start_node]
	y = {node: [] for node in g.nodes}
	while stack:
		elem = stack.pop()
		x.append(elem)
		for node in list(g.neighbors(elem)):
			if node not in x:
				stack.append(node)
				y[node].extend((*y[elem], elem))
	print(y)
	return "".join(x)
