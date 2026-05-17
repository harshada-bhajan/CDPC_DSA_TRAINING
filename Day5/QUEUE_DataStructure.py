import sys

class Queue:
    
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.queue.append(ele)
            print("Inserted:", ele)

    def delete(self):
        if self.isEmpty():
            queue is empty
        else:
            ele=self.queue[self.front]
            for i in range(1,self.rear+1):
                self.queue[i-1]=self.queue[i]
            self.rear-=1
        return ele
    
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[0])
            print("Last element:", self.queue[self.rear])
            
    def traverse(self):
        for i in range(self.front, self.rear+1):
            print(self.queue[i])
    
    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

if __name__ == '__main__':
    obj=Queue()
    
    while True:
        print("1. insert")
        print("2. delete")
        print("3. peek")
        print("4. traverse")
        print("0. Exit")

        ch=int(input("select any choice: "))
        
        if ch==1:
            ele=int(input("Enter data: "))
            obj.insert(ele)
            
        elif ch==2:
            obj.delete()
            
        elif ch==3:
            obj.peek()
            
        elif ch==4:
            obj.traverse()
            
        elif ch==0:
            sys.exit(0)
