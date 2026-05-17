import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5

    def isFull(self):
        return self.top == self.CAPACITY - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
            self.stack.append(ele)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele


class Queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    def isFull(self):
        return self.rear == self.CAPACITY - 1

    def isEmpty(self):
        return self.rear == -1

    def insert(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.queue.append(ele)

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        else:
            ele = self.queue[self.front]
            for i in range(1, self.rear + 1):
                self.queue[i - 1] = self.queue[i]
            self.queue.pop()
            self.rear -= 1
            return ele

    def traverse(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue elements:")
            for i in range(self.rear + 1):
                print(self.queue[i])

if __name__ == '__main__':
    obj1 = Queue()
    obj2 = Stack()

    n = int(input("Enter number of elements: "))

    for i in range(n):
        ele = int(input("Enter element: "))
        obj1.insert(ele)

    for i in range(n):
        obj2.push(obj1.delete())
        
    for i in range(n):
        obj1.insert(obj2.pop())

    obj1.traverse()







    
