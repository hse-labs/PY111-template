from typing import Any
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Any) -> dict:
	"""
	Count shortest paths from starting node to all nodes of graph g
	:param g: Graph from NetworkX
	:param starting_node: starting node from g
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
	"""
	paths_cost = {i: float('inf') for i in list(g.nodes)}
	paths_cost[starting_node] = 0
	not_visited = list(g.nodes)
	while not_visited:
		i = min(not_visited, key=lambda x: paths_cost[x])
		for j in g[i]:
			if (paths_cost[i] + g[i][j]['weight']) < paths_cost[j]:
				paths_cost[j] = paths_cost[i] + g[i][j]['weight']
		not_visited.remove(i)
	print(g, starting_node)
	return paths_cost
