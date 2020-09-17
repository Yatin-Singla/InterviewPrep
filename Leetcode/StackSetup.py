class Node:
    def __init__(self, data: int, next: Node = None):
        self.data = data
        self.next = next


class Stack:
    count = 0

    def __init__(self, head: Node = None):
        self.top = head
        if head != None:
            self.count += 1
        return

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data

    def isEmpty(self):
        return self.top == None

    def pop(self):
        if self.isEmpty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return data

    def push(self, data: int):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.count += 1
        return True

    def __pop(self):
        if not self.isEmpty():
            head = self.top
            self.top = self.top.next
            head.next = None
            self.count -= 1
            return head

    def popNode(self):
        return self.__pop()

    @staticmethod
    def RollOver(dest: Stack, src: Stack):
        while not src.isEmpty():
            dest.push(src.pop())
