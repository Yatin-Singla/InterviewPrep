class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

    def setNext(self, next):
        self.next = next


def PrintSLL(head: Node):
    while head != None:
        print(head.data, end=" -> ")
        head = head.next

    print()


def getLength(head: Node) -> int:
    length = 0
    while head != None:
        length += 1
        head = head.next

    return length


def Append(head: Node, item: Node) -> Node:
    if head == None:
        return item

    currPtr = head

    while currPtr.next != None:
        currPtr = currPtr.next

    currPtr.next = item
    return head


# new LL reversed
def deepRevSLL(head: Node) -> Node:
    if head == None:
        return head
    if head.next == None:
        return Node(head.data)

    RevLLHead = deepRevSLL(head.next)
    Append(RevLLHead, Node(head.data))
    return RevLLHead


# Iterative
def RevClone(head: Node):
    curr = None
    while head != None:
        clone = Node(head.data)
        clone.next = curr
        curr = clone
        head = head.next

    return curr
