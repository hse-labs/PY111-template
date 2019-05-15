from typing import Any
import networkx as nx


def dfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	visited_nodes = []
	nodes_stack = [start_node]
	while nodes_stack:
		node = nodes_stack.pop()
		visited_nodes.append(node)
		for edge in g.edges:
			if node in edge:
				if edge[1] not in visited_nodes:
					nodes_stack.append(edge[1])
				if edge[0] not in visited_nodes:
					nodes_stack.append(edge[0])
	return visited_nodes
