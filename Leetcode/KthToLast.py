'''
Implement an algorithm to find the kth to lsat element of a singly linked List
'''
from LLSetup import Node
import LLSetup

def GetKGap(head: Node, gap: int) -> Node:
    while head.next != None and gap > 1:
        head = head.next
        gap -= 1
    return head

def FindKthToLast(head: Node, gap: int):
    FPtr = GetKGap(head, gap)
    currPtr = head
    while Fptr.next != None:
        Fptr = Fptr.next
        currPtr = currPtr.next

    return currPtr

if __name__ == "__main__":
    print(FindKthToLast(Node(3, Node(2, Node(3, Node(1, Node(7, Node(9)))))), 3).data)