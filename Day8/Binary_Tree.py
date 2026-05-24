#Implementation of Binary Tree

import sys

class BST:
    def __init__(self, key):
        self.leftChild = None
        self.data = key
        self.rightChild = None

    def insert(self, key):
        if self.data is None:        
            self.data = key
            return

        if key == self.data:
            return
        elif key < self.data:
            if self.leftChild:
                self.leftChild.insert(key)
            else:
                self.leftChild = BST(key)
        else:
            if self.rightChild:
                self.rightChild.insert(key)
            else:
                self.rightChild = BST(key)

    def search(self, key):
        if self.data is None:
            print("Tree is empty")
            return

        if key == self.data:
            print(f"{key} found")
        elif key < self.data:
            if self.leftChild:
                self.leftChild.search(key)
            else:
                print(f"{key} not found")
        else:
            if self.rightChild:
                self.rightChild.search(key)
            else:
                print(f"{key} not found")

    def preorder(self):
        if self.data is None:
            return
        print(self.data, end=" -> ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.data, end=" -> ")

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.data, end=" -> ")
        if self.rightChild:
            self.rightChild.inorder()


if __name__ == '__main__':
    root = BST(None)

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Preorder")
        print("4. Postorder")
        print("5. Inorder")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 66]
            for x in arr:
                root.insert(x)
            print("Inserted successfully")

        elif n == 2:
            key = int(input("Enter value to search: "))
            print(root.search(key))

        elif n == 3:
            root.preorder()

        elif n == 4:
            root.postorder()

        elif n == 5:
            root.inorder()

        elif n == 0:
            sys.exit()
