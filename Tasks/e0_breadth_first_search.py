from typing import Any
import networkx as nx


def bfs(g: nx.Graph, start_node: Any) -> list:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visited_nodes = [start_node]
    nodes_queue = [start_node]
    while nodes_queue:
        node = nodes_queue[0]
        del nodes_queue[0]
        for edge in g.edges:
            if node in edge:
                if edge[1] not in visited_nodes:
                    nodes_queue.append(edge[1])
                    visited_nodes.append(edge[1])
                if edge[0] not in visited_nodes:
                    nodes_queue.append(edge[0])
                    visited_nodes.append(edge[0])
    return visited_nodes

