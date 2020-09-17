"""
Imagine a literal stack of plates. I fhte stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetofStacks that mimics this.
Set of Stacks should be composed of several stacks and should create a new stack once the previous one exceeds capactiy
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack 
(that is, pop() shuold return the same values as it would if there were just a single stack)
"""

from StackSetup import Stack
from StackSetup import Node

'''
    Node:                   Stack:              StackNode:                      SetofStacks:
        data: int               top: Node               data: Stack                     top: StackNode
        next: Node                                      next: StackNode
'''

class StackNode:
    def __init__(self, thresholdVal: int, data: Stack = None):
        self.data = Stack()
        self.next = None
        self.thresholdVal = thresholdVal

    def isEmpty(self):
        if self.data == None:
            return True
        else:
            return False
    
    def reachedThreshold():
        return self.data.count < self.thresholdVal




class SetOfStacks(Stack):
    def __init__(self, GivenThreshold: int):
        self.maxSize = GivenThreshold
        self.top = StackNode(thresholdVal: GivenThreshold)
        self.count = 1

    def reachedThreshold(self) -> bool:
        return self.top.reachedThreshold()

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            False
    
    def push(self, item: int):
        if self.reachedThreshold():
            newStackNode = StackNode(thresholdVal: maxSize, data: Stack(Node(item)))
            newStackNode.next = self.top
            self.top = newStackNode
            self.count += 1
        else:
            self.top.data.push(item)

    def pop():
        #set of stack's empty?
        if self.isEmpty():
            return None
        else:
            #top stacknode's empty?
            if self.top.isEmpty():
                return None
            else:
                #top stacknode's stack empty?
                if self.top.data.isEmpty():
                    return None
                else:
                    data = self.top.data.pop()
                    if self.top.data.count == 0:
                        self.top = self.top.next

    def helperPopAt(index)
        CurrPtr = self.top
        while index != 1:
            CurrPtr = CurrPtr.next
            index -= 1

        return CurrPtr

    def popAt(index: int):
        if self.count < index:
            return
        if index <= 0:
            return
        else:
            stack = helperPopAt(index)
            stack.data.pop()


if __name__ == "__main__":
    