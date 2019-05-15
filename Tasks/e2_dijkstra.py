from typing import Any
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Any) -> dict:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    visited_nodes = []
    cost_dict = {node: float('inf') if node != starting_node else 0 for node in g.nodes}

    while len(visited_nodes) < len(g.nodes):

        min_node = min(filter(lambda key: key not in visited_nodes, cost_dict), key=lambda key: cost_dict[key])

        for edge in g.edges:
            if edge[0] == min_node and edge[1] not in visited_nodes:
                if cost_dict[edge[1]] > cost_dict[edge[0]] + g[edge[0]][edge[1]]['weight']:
                    cost_dict[edge[1]] = cost_dict[edge[0]] + g[edge[0]][edge[1]]['weight']

        visited_nodes.append(min_node)

    return cost_dict
