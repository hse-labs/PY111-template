from typing import Any
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra_algo(g: nx.DiGraph, starting_node: Any) -> dict:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    node_weights = {node: float('inf') for node in g.nodes}
    queue = [starting_node]
    node_weights[starting_node] = 0
    while queue:
        element = queue.pop(0)
        for node, edg in g[element].items():
            route_weight = node_weights[element] + edg['weight']
            if node_weights[node] > route_weight:
                node_weights[node] = route_weight
                queue.append(node)
    return node_weights


if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_nodes_from([i for i in "ABCDEFG"])
    graph.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])
    nx.draw(graph, with_labels=True,)
    plt.show()
    print(dijkstra_algo(graph, 'A'))
