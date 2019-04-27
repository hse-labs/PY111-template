from typing import Any
import networkx as nx
import Tasks.a0_my_stack as st

import matplotlib.pyplot as plt


def dfs(g: nx.Graph, start_node: Any) -> list:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    re = ""
    q = []
    st.push(start_node)
    while st.length() > 0:
        vs = st.pop()
        q.append(vs)
        v = list(g.neighbors(vs))
        for i in v:
            if i not in q:
                st.push(i)
    for i in q:
        re += i
    return re
