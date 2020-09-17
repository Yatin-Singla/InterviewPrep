"""
Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack,
but you may not copy the elements into any other data structure (such as an array). The stack suppports the following operations:
push, pop, peek, and isEmpty.
"""

from StackSetup import *

def inOrder(givenStack: Stack):
    tempStack = Stack(givenStack.popNode())

    while not givenStack.isEmpty():
        if givenStack.peek() >= tempStack.peek():
            tempStack.push(NodegivenStack.pop()))
        else:
            Stack.RollOver(givenStack, tempStack)
            return False

    Stack.RollOver(givenStack, tempStack)
    return True

def inSort(givenStack: Stack):
    tempData = givenStack.pop()
    tempStack = Stack()
    while givenStack.peek() < tempData:
        tempStack.push(Node(givenStack.pop()))
    givenStack.push(Node(tempData))
    Stack.RollOver(givenStack, tempStack)
    return
        
def SortStack(givenStack: Stack):
    while not inOrder(givenStack):
        inSort(givenStack)