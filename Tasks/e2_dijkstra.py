from typing import Any
import networkx as nx
import Tasks.a0_my_stack as st

def dijkstra_algo(g: nx.DiGraph, starting_node: Any) -> dict:
	"""
	Count shortest paths from starting node to all nodes of graph g
	:param g: Graph from NetworkX
	:param starting_node: starting node from g
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
	"""
	print(g, starting_node)
	st.push(starting_node)
	q = []
	d = {}
	while st.length() > 0:
		vs = st.pop()
		q.append(vs)
		if vs in d:
			d[vs] += """"""
		else:
			d[vs] = """"""
		v = list(g.neighbors(vs))
		for i in v:
			if i not in q:
				st.push(i)
	return d
