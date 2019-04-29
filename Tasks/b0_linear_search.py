"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	minimum_element = arr[0]

	for element in arr:
		if element <= minimum_element:
			minimum_element = element

	return minimum_element


def min_weight_search(graph) -> tuple:
	"""
	Function that find edge in graph with minimal weight of all

	:param graph: NetworkX Graph (or digraph) with weighted edges
	:return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
	"""

	minimum_edge = 0
	minimum_nodes = []

	for edge in graph.edges():

		edge_weight = graph.get_edge_data(*edge)['weight']

		if edge_weight <= minimum_edge:
			minimum_edge = graph.get_edge_data(*edge)['weight']

	for edge in graph.edges():

		edge_weight = graph.get_edge_data(*edge)['weight']

		if edge_weight == minimum_edge:
			minimum_nodes.append(edge)

	return tuple(minimum_nodes)
