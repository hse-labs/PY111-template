from typing import Any
import networkx as nx
import Tasks.a0_my_stack as s


def dfs(g: nx.Graph, start_node: Any) -> list:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visited = []
    s.push(start_node)
    while s.my_stack:
        i = s.pop()
        if i not in visited:
            visited.append(i)
            for j in g[i].keys():
                if j not in visited:
                    s.push(j)
    print(g, start_node)
    return list(visited)
