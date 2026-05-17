# ============================================================
# CDPC DSA Training – Day 4
# Topic: Classes, Constructors & Stack Operations
# Language: Python
# ============================================================


# -----------------------------------------------------------
# Program 1: Class in Python (Basic Example)
# -----------------------------------------------------------
class Student:
    def show(self):
        print("I am in show")

s = Student()
s.show()


# ------------------------------------------------------------
# Program 2: Constructor in Python
# ------------------------------------------------------------

class Student:
    def __init__(self):
        print("default constructor ")

    def show(self):
        print("I am in show")

s = Student()
s.show()


# Constructor Overloading Example
class Student:
    def __init__(self, a, b):
        print(a, b)

    def show(self):
        print("I am in show")

s = Student(11, 22)
s.show()



# ------------------------------------------------------------
# Program 3: Stack Implementation (With Fixed Capacity)
# ------------------------------------------------------------

import sys

class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
        
    def isFull(self):
        if self.top==self.CAPACITY-1:
            return True
        else:
            return False
        
    def push(self,ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele, "is pushed")
            
    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])
            
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            stack is empty
        else:
            ele=self.stack[self.top]
            self.stack.pop()
            self.top-=1
        return ele
            
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]
        print("stack is full")

if __name__ == '__main__':
    obj=Stacks()
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch=int(input("Select any Choice"))
        if ch==1:
            
            ele=int(input("Enter data: "))
            obj.push(ele)
            
        elif ch==2:
            ele=int(input("is popped"))
            obj=obj.pop()
            
        elif ch==3:
            obj.peek()
        elif ch==4:
            obj.traverse()
        elif ch==0:
            sys.exit()
    

# ------------------------------------------------------------
# Program 4: Stack Implementation (Without Capacity)
# ------------------------------------------------------------
import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        
    def push(self, ele):
        self.top = self.top + 1
        self.stack.append(ele)
        print(ele, "is pushed")
            
    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])
            
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return None
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            print(ele, "is popped")
            return ele
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[self.top])

if __name__ == '__main__':
    obj = Stacks()
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch = int(input("Select any Choice: "))

        if ch == 1:
            ele = int(input("Enter data: "))
            obj.push(ele)
            
        elif ch == 2:
            obj.pop()
            
        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit()


# ------------------------------------------------------------
# Program 5: Reverse Stack Using Stack Operations
# ------------------------------------------------------------
import sys

class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 10
        
    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False
        
    def push(self, ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")
            
    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])
            
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return None
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

if __name__ == '__main__':
    obj=Stacks()
    arr=[234235, 235, 235, 235, 5]
    rev=[]
    for i in range(len(arr)):
        obj.push(arr[i])
        
    for i in range(len(arr)):
        ele=obj.pop()
        rev.append(ele)
    print rev



            









        
















