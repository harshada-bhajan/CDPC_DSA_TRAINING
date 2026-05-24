#Singly Linked List Implementation in Python

import sys

class GetNode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newNode

        print(data, "is added")

    def traverse(self):

        if self.head == None:
            print("Linked List not Present")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, " -> ", end="")

                ptr = ptr.next

            print("None")
            
    def addbegin(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        newNode.next = self.head
        self.head = newNode

        print(data, "node added at beginning")


    def addbetwn(self):

        data = int(input("Enter data: "))
        key = int(input("Enter data after inserted: "))

        newNode = GetNode()
        newNode.data = data

        if self.head == None:
            print("Linked List not Present")

        else:
            ptr = self.head

            while ptr != None:

                if key == ptr.data:
                    break

                ptr = ptr.next

            if ptr == None:
                print("Key not found")

            else:
                newNode.next = ptr.next
                ptr.next = newNode

                print(data, "is added")


    def addend(self):

        data = int(input("Enter data: "))

        newNode = GetNode()
        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newNode

        print(data, "node added at end")

    
    def Deltbeg(self):

        if self.head == None:
            print("List not present")

        else:
            ptr = self.head
            self.head = ptr.next

            print(ptr.data, "is deleted.")


    def DeltBetween(self):

        key = int(input("Enter node value to delete: "))

        if self.head == None:
            print("List not present")

        elif self.head.data == key:

            ptr = self.head
            self.head = ptr.next

            print(ptr.data, "is deleted.")

        else:
            ptr = self.head

            while ptr.next != None:

                if ptr.next.data == key:
                    break

                ptr = ptr.next

            if ptr.next == None:
                print("Node not found")

            else:
                temp = ptr.next
                ptr.next = temp.next

                print(temp.data, "is deleted.")

    def DeltEnd(self):

        if self.head == None:
            print("List not present")

        elif self.head.next == None:

            print(self.head.data, "is deleted.")
            self.head = None

        else:
            ptr = self.head

            while ptr.next.next != None:
                ptr = ptr.next

            print(ptr.next.data, "is deleted.")
            ptr.next = None


if __name__ == '__main__':

    obj = LinkedList()

    while True:

        print("\n1. Append")
        print("2. Traverse")
        print("3. Add Beginning")
        print("4. Add Between")
        print("5. Add End")
        print("6. Delete Beginning")
        print("7. Delete Between")
        print("8. Delete End")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 3:
            obj.addbegin()

        elif n == 4:
            obj.addbetwn()

        elif n == 5:
            obj.addend()

        elif n == 6:
            obj.Deltbeg()

        elif n == 7:
            obj.DeltBetween()

        elif n == 8:
            obj.DeltEnd()

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid Choice")
