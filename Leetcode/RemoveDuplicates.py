'''
Write a program to remove duplicates from an unsorted linked list.
'''
class Node:
    def __init__(self, data: int, next = None):
        self.data = data
        self.next = next

#   O(n)        O(n)
def RemoveDuplicates(head: Node) -> Node:
    if not head:
        return head

    hashTable = {head.data:1}
    currPtr, prevPtr = head.next, head
    while currPtr != None:
        if currPtr.data not in hashTable:
            hashTable[currPtr.data] = 1
        else:
            prevPtr.next = currPtr.next
        
        prevPtr = prevPtr.next
        currPtr = currPtr.next
    
    return head

# Solution 2
#   O(n^2)      O(1)
def RMDupwBuffer(head: Node):
    currPtr = head
    while currPtr != None:
        runner = currPtr
        while runner.next != None:
            if runner.next.data == currPtr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currPtr = currPtr.next
    return head

def PrintSL(head: Node):
    while head != None:
        print(head.data, end=' ')
        head = head.next

if __name__ == "__main__":
    PrintSL(RMDupwBuffer(Node(3, Node(2, Node(3, Node(1, Node(7)))))))

