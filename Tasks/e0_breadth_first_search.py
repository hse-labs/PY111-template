from typing import Any
import networkx as nx
import Tasks.a1_my_queue as q   # вместо append() можно использовать свой модуль queue и

import matplotlib.pyplot as plt

def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	visited = [start_node]
	queue = [start_node]

	while len(queue) != 0:
		active_node = queue.pop(0)
		for neighbour in g[active_node]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)


#g = nx.Graph()

# 	g.add_node("a")
#
# 	g.add_nodes_from(["b", "c"])
# #	G.add_edge('f', 'd')
# 	g.add_edge('f', 'd', weight=3.7)
# 	G.add_edges_from([('e', 'r'),('t','q')])


	# print(g.nodes())
	# print(g.edges())
	# print(list(g.neighbors('e')))
	# print(g['f'])
	# nx.draw(g, with_labels=True)
	# plt.show()

    # print(g, start_node)
	# return list(g.nodes)
	print(g.nodes)
	print(visited)
	return(visited)



bfs(nx.Graph([('a','b'), ('a','f'), ('b','g'), ('f', 'g'), ('g','i'), ('g','c'), ('c','h'), ('i','h'), ('h','j'), ('h','d'), ('d','e'), ('g','h'), ('h','e')]),'a')