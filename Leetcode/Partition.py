'''
Write code to partition a linked list around a value x, such that all nodes less than x come 
before all node greater than or equal to x. if x is contained within the list, 
the values of x only need to be after the elements less than x.
The partition element x can appear anywhere in the "right partition";
it does not need to appear betrween left and right partitions.
'''
from LLSetup import *

def Append(head: Node, tail: Node, next: Node):
    if head == None:
        head = tail = next
    else:
        tail.next = next
        tail = tail.next

    return head, tail

def Partition(head: Node, partition: int) -> Node:
    lowH = lowT = midH = midT = highH = highT = None
    while head != None:
        if head.data < partition:
            lowH, lowT = Append(lowH, lowT, Node(head.data))
        elif head.data == partition:
            midH, midT = Append(midH, midT, Node(head.data))
        else: # head.data > parttion:
            highH, highT = Append(highH, highT, Node(head.data))

        head = head.next

    midH, midT = Append(midH, midT, highH)
    lowH, lowT = Append(lowH, lowT, midH)

    return lowH

if __name__ == "__main__":
    PrintSLL(Partition(Node(3,Node(5, Node(8, Node(5, Node(10, Node(2, Node( 1))))))),5))
    
