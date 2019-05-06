from typing import Any
import networkx as nx


def dfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)
