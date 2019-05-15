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
			stack.extend(g[vertex])

	return visited