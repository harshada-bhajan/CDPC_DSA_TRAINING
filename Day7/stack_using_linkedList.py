#Implementation of Stack Using Linked List

import sys

class GetNode:
    def __init__(self):
        self.data=None
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def push(self):
        data=int(input("Enter data: "))

        newNode=GetNode()
        newNode.data=data

        if self.top==None:
            self.top=newNode

        else:
            newNode.next=self.top
            self.top=newNode

        print(data,"is pushed into stack")

    def pop(self):
        if self.top==None:
            print("Stack Underflow")

        else:
            ptr=self.top
            self.top=ptr.next

            print(ptr.data,"is popped")

    def traverse(self):
        if self.top==None:
            print("Stack is Empty")

        else:
            ptr=self.top
            
            while ptr!= None:
                print(ptr.data)
                ptr = ptr.next

    def peek(self):
        if self.top == None:
            print("Stack Empty")
            
        else:
            print("Top element is:", self.top.data)


if __name__ == '__main__':
    obj = Stack()

    while True:
        print("\n1. Push")
        print("\n2. Pop")
        print("\n3. traverse")
        print("\n4. Peek")
        print("\n0. Exit")
        n = int(input("Enter choice: "))

        if n==1:
            obj.push()

        elif n==2:
            obj.pop()

        elif n==3:
            obj.traverse()

        elif n==4:
            obj.peek()

        elif n==0:
            sys.exit(0)

        else:
            print("Invalid Choice")
