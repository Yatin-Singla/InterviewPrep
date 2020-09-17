# Question: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
# (eg if you have a tree with depth D, you'll have D linkedlists)

# Solution

from treeNode import Node
from queue import LifoQueue as Queue


# helper function


def Process(node, level, result):
    if level > len(result) - 1:
        result.append([node])
    else:
        result[level].append(node)

    return


# BFS implementation
def ListDepths(root: Node):
    if not root:
        return
    Q = Queue()
    level, result = 0, []
    Q.enqueue((root, level))

    while not Q.isEmpty():
        node, level = Q.dequeue()
        Process(node, level, result)
        if node.left:
            Q.enqueue((node.left, level + 1))
        if node.right:
            Q.enqueue((node.right, level + 1))

    return result


# DFS helper

"""
Assumption: 
    value of level would be atmost 1 > len(result)
    passing in reference
"""


def DFSHelper(root, level, result):
    if not root:
        return

    if level > len(result) - 1:
        result.append([root])
    else:
        result[level].append(root)

    DFSHelper(root.left, level + 1, result)
    DFSHelper(root.right, level + 1, result)

    return


# DFS


def DFSlistDepth(root: Node):
    level, result = 0, []
    DFSHelper(root, level, result)
    return result
