from typing import Any
import networkx as nx


def dfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""

	explored_nodes = [start_node]  # посещённые вершины
	stack = [start_node]

	while stack:
		nb = list(g.neighbors(stack.pop()))

		for i in nb:
			if i not in explored_nodes:
				explored_nodes.append(i)
				stack.append(i)
	print(g, start_node)

	return explored_nodes


