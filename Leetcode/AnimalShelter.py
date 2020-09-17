"""
An animal shelter which holds only dogs, and cats, operates on a strictly "first in, first out" basis.
Perople must adopt either the "oldest" (based on arrival time) of all animals at teh shelter,
or they can select whetherthey would prefer a dog or a cat (and will receive the oldest animal of that type)
They cannot select which specific animal they would like. 
Create the data structure to maintain this system adn implement operations such as enqueue, dequeueAny,
dequeueDog, and dequeueCat.
"""
from QueueSetup import Queue


class Dog(Node):
    def __init__(self, age: int):
        super.__init__(age)


class Cat(Node):
    def __init__(self, age: int):
        super.__init__(age)


class AnimalShelter(Queue):
    def __init__(self):
        self.dogQueue = Queue()
        self.catQueue = Queue()
        self.counter = 1

    def enqueue(self, animal: Node):
        animal.data = self.counter
        self.counter += 1
        if animal is Dog:
            self.dogQueue.enqueue(animal)
        else:
            self.catQueue.enqueue(animal)

    def dequeueDog(self):
        return self.dogQueue.dequeue()

    def dequeueCat(self):
        return self.catQueue.dequeue()

    def dequeue(self):
        return (
            self.dogQueue.dequeue()
            if self.dogQueue.peek() > self.catQueue.peek()
            else self.catQueue.dequeue()
        )
