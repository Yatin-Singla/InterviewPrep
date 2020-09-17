'''
Given a circular linked list, implement an algorithm that returns the node oat the beginning of the loop
'''
from LLSetup import Node

def detectLoop(head: Node) -> Node:
    if head == None:
        return None

    Visited = set()
    while head not in Visited:
        Visited.add(head)
        head = head.next

    return head

if __name__ == "__main__":
    A = Node(5, None)
    B = Node(7, None)
    C = Node(0, None)
    D = Node(1, None)
    E = Node(2, C)
    A.setNext(B)
    B.setNext(C)
    C.setNext(D)
    D.setNext(E)
    data = detectLoop(A)
    print(data.data)
