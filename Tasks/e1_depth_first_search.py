from typing import Any
import networkx as nx


def dfs(g: nx.Graph, start_node: Any) -> str:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	stack = [start_node]
	visited = []
	while stack:
		i = stack[-1]
		for j in g[i]:
			if j not in visited:
				stack.append(j)
		visited.append(i)
		stack.remove(i)
	print(g, start_node)
	return ''.join(visited)
