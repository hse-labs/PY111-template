from typing import Any
import networkx as nx


def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	queue = [start_node]
	visited = [start_node]
	paths = {i: [i] for i in list(g.nodes)[1:]}
	while queue:
		for i in queue:
			for j in g[i]:
				if j not in visited:
					visited.append(j)
					queue.append(j)
					paths[j] = paths[i] + paths[j]
			del queue[0]
	print(g, start_node)
	return visited
