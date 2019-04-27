from typing import Any
import networkx as nx
import Tasks.a1_my_queue as queue
# import matplotlib.pyplot as plt


def bfs(g: nx.Graph, start_node: Any) -> list:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    q = [start_node]
    queue.enqueue(start_node)
    while queue.length() > 0:
        v = list(g.neighbors(queue.dequeue()))
        for i in v:
            if i not in q:
                q.append(i)
                queue.enqueue(i)
    return q
