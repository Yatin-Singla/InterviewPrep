"""
Impleement a MyQueue class which implements a queue using two stacks
"""

from StackSetup import *


class MyStack(Stack):
    def __pop(self):
        if not self.isEmpty():
            head = self.top
            self.top = self.top.next
            head.next = None
            self.count -= 1
            return head

    def __push(self, data: Node):
        data.next = self.top
        self.top = data
        self.count += 1
        return


class MyQueue:
    def __init__(self):
        self.insertStack = MyStack()
        self.deletionStack = MyStack()

    def __RollOver(self):
        if self.insertStack.isEmpty():
            while not self.deletionStack.isEmpty():
                self.insertStack.__push(self.deletionStack.__pop())
        else:
            while not self.insertStack.isEmpty():
                self.deletionStack.__push(self.insertStack.__pop())

    def push(self, item: int):
        if self.insertStack.isEmpty():
            self.__RollOver()

        return self.insertStack.push(item)

    def pop(self):
        if self.deletionStack.isEmpty():
            self.__RollOver()

        return self.deletionStack.pop()

    def peek(self):
        if self.insertStack.isEmpty():
            self.__RollOver()

        return self.insertStack.peek()
