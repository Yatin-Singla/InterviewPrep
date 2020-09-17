'''
Fiven two (Singly) linked lists, determine if the two lists intersect. Return the intersection node.
Node that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the the exact same onde (by reference) as the jth
node of hte second linked list, then they are intersecting.
'''
from LLSetup import Node, getLength
from QueueSetup import Queue

# O(n2)
def DetectIntersection(list1H: Node, list2H: Node) -> bool:
    while list1H != None:
        checkPtr = list2H
        while checkPtr != None:
            if list1H == checkPtr:
                return True
            checkPtr = checkPtr.next
        list1H = list1H.next

    return False

# O(n)
def detectIntersection(list1H: Node, list2H: Node) -> bool:
    if list1H == None or list2H == None:
        return false

    while (list1H.next != None):
        list1H = list1H.next
    while (list2H.next != None):
        list2H = list2H.next

    return list1H == list2H

#step 1: iterate to end of both lists
#step 2: check if the last element of both lists' is ==
#step 3: if False, return else iterate through the longer list = diff in len of lists
#step 4: return element where they intersect
def returnIntersectionNode(PNode: Node, SNode: Node) -> Node:
    if PNode == None or SNode == None:
        return 0
    
    PList, SLode = PNode, SNode
    PLen = SLen = 1
    #step 1
    while(PList.next != None):
        PList = PList.next
        PLen += 1
    while(SList.next != None):
        SList = SList.next
        SLen += 1
    #step 2
    if PList != SList:
        return None

    #step 3
    if PLen > SLen:
        for i in range(PLen-SLen):
            PNode = PNode.next
    elif PLen < SLen:
        for i in range(SLen-PLen):
            SNode = SNode.next
    
    # step 4
    while(PNode != SNode):
        PNode = PNode.next
        SNode = SNode.next
    
    return PNode

        




if __name__ == "__main__":
    commonList = Node(7, Node(4, Node(5, Node(-1, Node(0)))))
    PList = Node(3, Node(20, Node(-7, commonList)))
    SList = Node(-5, Node(1, Node(-11, Node(8, Node(-4, Node(-2, commonList))))))
    print(detectIntersection(PList,SList))

