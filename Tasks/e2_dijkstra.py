from typing import Any
import networkx as nx
import Tasks.a1_my_queue as q


def dijkstra_algo(g: nx.DiGraph, starting_node: Any) -> dict:
	"""
	Count shortest paths from starting node to all nodes of graph g
	:param g: Graph from NetworkX
	:param starting_node: starting node from g
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
	"""
	dict_of_distances = dict()
	dict_of_distances[starting_node] = 0
	q.enqueue(starting_node)
	while q.my_queue:
		v = q.dequeue()
		for u in g[v]:
			if u not in dict_of_distances or dict_of_distances[v] + g[v][u]['weight'] < dict_of_distances[u]:
				dict_of_distances[u] = dict_of_distances[v] + g[v][u]['weight']
				q.enqueue(u)
	for i in g.nodes:
		if i not in dict_of_distances.keys():
			dict_of_distances[i] = float("inf")
	return dict_of_distances
