from LLSetup import Node

# returns the middle element of the list
def MiddleList(head: Node) -> Node:
    if head == None:
        return None
    slow = fast = head
    while(fast.next != None and fast.next.next != None):
        fast = fast.next.next
        slow = slow.next

    return slow

if __name__ == "__main__":
    data = MiddleList(Node(3, Node(7, Node(4, Node(-1, Node(5, Node(6)))))))
    print(data.data)