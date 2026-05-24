#Implementation of Doubly-Linked List in python

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self):

        data = int(input("Enter data: "))
        newnode = Node(data)

        if self.head is None:
            self.head = newnode

        else:
            ptr = self.head

            while ptr.right is not None:
                ptr = ptr.right

            ptr.right = newnode
            newnode.left = ptr

        print(data, "is added")

    def traverse(self):

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr = self.head

            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.right

            print("None")

    def addbegin(self):

        data = int(input("Enter data: "))
        newnode = Node(data)

        if self.head is None:
            self.head = newnode

        else:
            ptr = self.head

            newnode.right = ptr
            ptr.left = newnode
            self.head = newnode

        print(data, "is added at beginning")


    def addatbetween(self):

        data = int(input("Enter data: "))
        key = int(input("Enter key: "))

        newnode = Node(data)

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr = self.head

            while ptr is not None and ptr.data != key:
                ptr = ptr.right

            if ptr is None:
                print("Key not found")

            else:
                newnode.right = ptr
                newnode.left = ptr.left

                if ptr.left is not None:
                    ptr.left.right = newnode

                ptr.left = newnode

                if ptr == self.head:
                    self.head = newnode

                print(data, "is added before", key)


    def addend(self):

        data = int(input("Enter data: "))
        newnode = Node(data)

        if self.head is None:
            self.head = newnode

        else:
            ptr = self.head

            while ptr.right is not None:
                ptr = ptr.right

            ptr.right = newnode
            newnode.left = ptr

        print(data, "is added at end")

    
    def delbegin(self):

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr = self.head
            self.head = ptr.right

            if self.head is not None:
                self.head.left = None

            print(ptr.data, "is deleted from beginning")


    def delbetween(self):

        key = int(input("Enter node value to delete: "))

        if self.head is None:
            print("Linked list is empty")

        else:
            ptr = self.head

            while ptr is not None and ptr.data != key:
                ptr = ptr.right

            if ptr is None:
                print("Node not found")

            elif ptr == self.head:
                self.head = ptr.right

                if self.head is not None:
                    self.head.left = None

                print(ptr.data, "is deleted")

            else:
                if ptr.right is not None:
                    ptr.right.left = ptr.left

                if ptr.left is not None:
                    ptr.left.right = ptr.right

                print(ptr.data, "is deleted")

    
    def delend(self):

        if self.head is None:
            print("Linked list is empty")

        elif self.head.right is None:
            print(self.head.data, "is deleted")
            self.head = None

        else:
            ptr = self.head

            while ptr.right is not None:
                ptr = ptr.right

            ptr.left.right = None

            print(ptr.data, "is deleted from end")


if __name__ == '__main__':

    obj = DoubleLinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. Add at Beginning")
        print("4. Add at Between")
        print("5. Add at End")
        print("6. Delete Beginning")
        print("7. Delete Between")
        print("8. Delete End")
        print("0. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            obj.append()

        elif ch == 2:
            obj.traverse()

        elif ch == 3:
            obj.addbegin()

        elif ch == 4:
            obj.addatbetween()

        elif ch == 5:
            obj.addend()

        elif ch == 6:
            obj.delbegin()

        elif ch == 7:
            obj.delbetween()

        elif ch == 8:
            obj.delend()

        elif ch == 0:
            sys.exit()

        else:
            print("Invalid Choice")
    
