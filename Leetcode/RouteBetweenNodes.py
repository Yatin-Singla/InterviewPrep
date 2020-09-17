# Question: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

# Explanation
""" 
I would like to use BFS instead of DFS as DFS might pigeonhole our search through neighbor's neighbor whereas the target 
might the next neighbor
Additionally I'm not using Bi-directional search because I'm not sure if there is a path from target to root, 
Worst case scenario efficiency would be the same
"""

# Solution:
from queue import LifoQueue as Queue


def BFS(start, finish) -> bool:
    if not start or not finish:
        return False
    Q = Queue()
    # marked is a flag to indicate that the node has already been enqueued
    start.marked = True
    Q.enqueue(start)

    # process all nodes
    while not Q.isEmpty():
        node = Q.dequeue()
        if node == target:
            return True
        for Neighbor in node.neighbors:
            if not Neighbor.marked:
                Neighbor.marked = True
                Q.enqueue(Neighbor)

    return True
