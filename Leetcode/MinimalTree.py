# Question: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

# Explanation
"""
! hint:
    node.left <= node <= node.right
    sorted array
"""

# Solution

from treeNode import Node


def MinimalTree(A: List[int]) -> Node:
    if not A:
        return None

    lenA = len(A)

    if lenA == 1:
        return Node(A[0])

    root = Node(A[lenA // 2])
    root.left = MinimalTree(A[: lenA // 2])
    root.right = MinimalTree(A[lenA // 2 :])

    return root
