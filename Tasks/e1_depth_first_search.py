from typing import Any
import networkx as nx
import matplotlib.pyplot as plt


def dfs(g: nx.Graph, start_node: Any) -> str:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visited = []
    stack = [start_node]
    tracks = {node: [] for node in g.nodes}
    while stack:
        element = stack.pop()
        visited.append(element)
        for node in list(g.neighbors(element)):
            if node not in visited:
                stack.append(node)
                tracks[node].extend((*tracks[element], element))
        # tracks[node].extend((*tracks[element], element))
        # for node in reversed(neighbors):
        # 	if node not in visited:
        # 		visited.append(node)
        # 		stack.append(node)
        # 		tracks[node].extend((*tracks[element], element))
    print(tracks)
    return "".join(visited)


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from(["ABCDEFG"])
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    result = dfs(graph, 'A')
    print(result)
    nx.draw(graph, with_labels=True)
    plt.show()
    print(result)
