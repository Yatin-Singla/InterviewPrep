"""
list
collections.deque
queue.LifoQueue
"""
from LLSetup import Node

# Queue implementation of a singly linked list
class Queue:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def enqueue(self, item: Node) -> bool:
        if self.isEmpty():
            self.head = self.tail = item
            return True
        else:
            self.tail.next = item
            self.tail = item
            return True

    def dequeue(self) -> Node:
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            if self.isEmpty():
                self.tail = None
            return temp

    def isEmpty(self) -> bool:
        return True if self.head == None else False

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
