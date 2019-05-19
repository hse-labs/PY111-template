import networkx as nx
import random

nodes = [1, 2, 3, 4, 5, 6]
edges = [[1, 2], [1, 3], [4, 5]]
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)
explored_nodes = []
count = 0


def bfs():
    global count
    start_node = random.choice(nodes)
    stack = [start_node]
    while stack:
        nb = list(graph.neighbors(stack.pop()))
        nb.append(start_node)
        for i in nb:
            if i not in explored_nodes:
                nodes.remove(i)
                explored_nodes.append(i)
                stack.append(i)
    count += 1


while nodes:
    bfs()

print("Число компонент связности графа: ", count)
