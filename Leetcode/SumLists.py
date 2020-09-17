"""
You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
input: (7->1->6) + (5->9->2) = 617+295
output: 2->1->9 = 912
"""
from LLSetup import *

# new LL reversed 
'''Deep Copy'''
def NewRevSLL(head: Node) -> Node:
    if head == None:
        return head
    if head.next == None:
        return Node(head.data)
    
    RevLLHead = RevSLL(head.next)
    Append(RevLLHead, Node(head.data))
    return RevLLHead

# same LL reversed
''' Shallow Copy'''
def RevSLL(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    
    RevLLHead = RevSLL(head.next)
    head.next.next = head
    head.next = None
    return RevLLHead

def normalAdd(num1: Node, num2: Node) -> Node:
    sum = carry = 0
    result = None
    while num1 != None:
        sum = num1.data + num2.data + carry 
        result = Append(result, Node(sum%10))
        carry = sum//10
        num1 = num1.next
        num2 = num2.next

    if carry:
        result = Append(result, Node(carry))

    return result

def diffLenAdd(longer: Node, shorter: Node) -> Node:
    sum = carry = 0
    result = None
    while shorter != None:
        sum = longer.data + shorter.data + carry 
        result = Append(result, Node(sum%10))
        carry = sum//10
        longer = longer.next
        shorter = shorter.next

    while longer != None:
        sum = longer.data + carry
        result = Append(result, Node(sum%10))
        carry = sum // 10
        longer = longer.next
    
    if carry:
        result = Append(result, Node(carry))

    return result


def sumList(num1: Node, num2: Node) -> Node:
    if num1 == None or num2 == Node:
        return num2 if num1 == None else num1

    len1 = getLength(num1)
    len2 = getLength(num2)    
    diff = len1-len2
   
    if diff == 0:
        return normalAdd(num1, num2)
    else:
        if diff > 0:
            return diffLenAdd(num1, num2)
        else:
            return diffLenAdd(num2, num1)

def sumListFollowUp(num1: Node, num2: Node) -> Node:
    return RevSLL(sumList(RevSLL(num1), RevSLL(num2)))

if __name__ == "__main__":
    num1 = Node(6, Node(1, Node(7)))
    num2 = Node(2, Node(9, Node(5)))
    PrintSLL(sumList(Node(7, Node(1, Node(6))), Node(5, Node(9, Node(2, Node(9))))))

    PrintSLL(sumListFollowUp(num1, num2))