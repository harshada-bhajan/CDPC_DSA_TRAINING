# Single Inheritance

class A:
    def showA(self):
        print("I am in class A")


class B(A):
    def showB(self):
        print("I am in class B")


if __name__ == '__main__':

    obj = B()

    obj.showA()
    obj.showB()
    







# Multilevel Inheritance


class A:
    def showA(self):
        print("I am in class A")


class B(A):
    def showB(self):
        print("I am in class B")


class C(B):
    def showC(self):
        print("I am in class C")


if __name__ == '__main__':

    obj = C()

    obj.showA()
    obj.showB()
    obj.showC()










# Multiple Inheritance


class A:
    def showA(self):
        print("I am in class A")


class B:
    def showB(self):
        print("I am in class B")


class C(A, B):
    def showC(self):
        print("I am in class C")


if __name__ == '__main__':

    obj = C()

    obj.showA()
    obj.showB()
    obj.showC()









# Hierarchical Inheritance


class A:
    def showA(self):
        print("I am in class A")


class B(A):
    def showB(self):
        print("I am in class B")


class C(A):
    def showC(self):
        print("I am in class C")


if __name__ == '__main__':

    obj1 = B()
    obj1.showA()
    obj1.showB()

    obj2 = C()
    obj2.showA()
    obj2.showC()











# Hybrid Inheritance

class A:
    def showA(self):
        print("I am in class A")


class B(A):
    def showB(self):
        print("I am in class B")


class C(A):
    def showC(self):
        print("I am in class C")


class D(B, C):
    def showD(self):
        print("I am in class D")


if __name__ == '__main__':

    obj = D()

    obj.showA()
    obj.showB()
    obj.showC()
    obj.showD()









# Polymorphism Example

class A:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            print(a + b + c)
        elif a and b:
            print(a + b)
        else:
            print(a)
obj = A()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)










#polymorphism overiding

class parent:
    def __init__(self):
        self.speed=100
        print("cash,gold")

    def bike(self):
        print("splender + ",self,speed)

class child(parent):
    def __init__(self):
        self.speed=150
    def bike(self):
        print("HB",self.speed)

obj=child()
obj.bike()







        
