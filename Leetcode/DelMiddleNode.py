'''
Implement an algorithm to delete node in the middle (any node but the first and last)
of a singly linked list, given only acess to that node
'''

from LLSetup import *

def DelMiddleNode(head: Node):
    head.data = head.next.data
    head.next = head.next.next

if __name__ == "__main__":
    head = Node(0, Node(1,Node(2, Node(3, Node(4, Node(5, Node(6)))))))
    DelMiddleNode(head.next.next.next)
    PrintSLL(head)