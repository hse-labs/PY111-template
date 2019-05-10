from typing import Any
import networkx as nx
import Tasks.a1_my_queue as q


def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	visited = []
	q.enqueue(start_node)
	while q.my_queue:
		i = q.dequeue()
		if i not in visited:
			visited.append(i)
			for j in g[i].keys():
				if j not in visited:
					q.enqueue(j)

	print(g, start_node)
	return list(visited)
