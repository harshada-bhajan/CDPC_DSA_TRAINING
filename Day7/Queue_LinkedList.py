#Implementation of Queue Data Structure using Linked List
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def append(self):
        data = int(input("Enter data: "))
        newNode = Node(data)

        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        print(data, "inserted into queue")

    def deleteAtBegin(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            print(temp.data, "deleted from queue")

            if self.front is None:
                self.rear = None

    def peekFront(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element is:", self.front.data)

   
    def peekRear(self):
        if self.rear is None:
            print("Queue is empty")
        else:
            print("Rear element is:", self.rear.data)

    def traverse(self):
        if self.front is None:
            print("Queue is empty")
        else:
            ptr = self.front
            while ptr:
                print(ptr.data, "->", end=" ")
                ptr = ptr.next
            print()



if __name__ == '__main__':
    q = Queue()

    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Peek Front")
        print("4. Peek Rear")
        print("5. Display")
        print("0. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            q.append()
        elif ch == 2:
            q.deleteAtBegin()
        elif ch == 3:
            q.peekFront()
        elif ch == 4:
            q.peekRear()
        elif ch == 5:
            q.traverse()
        elif ch == 0:
            sys.exit(0)
        else:
            print("Invalid choice")




#single Linked List
import sys

class GetNode:
	def __init__(self,data):
		self.data=data
		self.link=None

class LinkedList:
	def __init__(self):
		self.head=None
		#ptr=GetNode()

	def append(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		#new_node.data=data

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.link is not None:
				ptr=ptr.link
			ptr.link=new_node
		print(data,"is added..")

	def traverse(self):
		ptr=self.head
		while ptr is not None:
			print(" -> ",ptr.data,end="")
			ptr=ptr.link

	def addAtBegin(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		#new_node.data=data

		if self.head is None:
			self.head=new_node
		else:
			new_node.link=self.head
			self.head=new_node
		print(data,"is added at begin..")
		

	def addAtAfter(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		key=int(input("Enter data after which data will be added: "))

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.link is not None:
				if key==ptr.data:
					break
				else:
					ptr=ptr.link
			if ptr.link is None:
				print(key," not found ")
			else:
				ptr1=ptr.link
				new_node.link=ptr1
				ptr.link=new_node
				print(data,"is added after ",key)

	def addAtBefore(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		key=int(input("Enter data before which data will be added: "))

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.link is not None:
				if key==ptr.data:
					break
				else:
					ptr1=ptr
					ptr=ptr.link
			if ptr.link is None:
				print(key," not found ")
			else:
				new_node.link=ptr
				ptr1.link=new_node
				print(data,"is added after ",key)


	def addAtEnd(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.link is not None:
				ptr=ptr.link
			ptr.link=new_node
		print(data,"is added at the end..")


	def deleteAtBegin(self):
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			ptr1=ptr.link
			ptr.link=None
			self.head=ptr1
		print(ptr.data,"is deleted from begin..")

	def deleteAtAfter(self):
		key=int(input("Enter data after which data will be added: "))

		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.link is not None:
				if key==ptr.data:
					break
				else:
					ptr=ptr.link
			if ptr.link is None:
				print(key," not found ")
			else:
				ptr1=ptr.link
				ptr2=ptr1.link
				ptr.link=ptr2
				ptr1.link=None
				print(ptr1.data," is deleted after ",key)
	

	def deleteAtValue(self):
		key=int(input("Enter data which node will be deleted: "))

		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.link is not None:
				if key==ptr.data:
					break
				else:
					ptr1=ptr
					ptr=ptr.link
					ptr2=ptr.link
			if ptr.link is None:
				print(key," not found ")
			else:
				
				ptr1.link=ptr2
				ptr.link=None
				print(ptr.data,"is deleted ",key)



	def deleteAtEnd(self):
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.link is not None:
				ptr1=ptr
				ptr=ptr.link
			ptr1.link=None
			print(ptr.data,"is deleted from the end..")	

	def length(self):
		len=0
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr is not None:
				len=len+1
				ptr=ptr.link
			print("Size of LinkedList is ",len)

obj=LinkedList()
if __name__ == '__main__':
	while True:
		print("\n\n1. Append\t\t2. Add At Begin  \t3. Add At After")
		print("4. Add At Before\t5. Add At End\t\t6. Delete At Begin")
		print("7. Delete At After\t8. Delete Ay Node\t9. Delete At End")
		print("10. Length\t\t11. Traverse\t\t0. Exit")
		n=int(input("Select your choice: "))
		if n==1:
			obj.append()
		elif n==2:
			obj.addAtBegin()
		elif n==3:
			obj.addAtAfter()
		elif n==4:
			obj.addAtBefore()
		elif n==5:
			obj.addAtEnd()
		elif n==6:
			obj.deleteAtBegin()
		elif n==7:
			obj.deleteAtAfter()
		elif n==8:
			obj.deleteAtValue()
		elif n==9:
			obj.deleteAtEnd()
		elif n==10:
			obj.length()
		elif n==11:
			obj.traverse()
		elif n==0:
			sys.exit()


#Doubly Linked-List
import sys

class GetNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

class LinkedList:
	def __init__(self):
		self.head=None
		#ptr=GetNode()

	def append(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		#new_node.data=data

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.right is not None:
				ptr=ptr.right
			ptr.right=new_node
			new_node.left=ptr
			print(data,"is added..")

	def traverseForward(self):
		ptr=self.head
		while ptr is not None:
			print(" ->",ptr.data,end="")
			ptr=ptr.right

	def traverseBackward(self):
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.right is not None:
				ptr=ptr.right

			while ptr is not None:
				print(" ->",ptr.data,end="")
				ptr=ptr.left

	def addAtBegin(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		#new_node.data=data

		if self.head is None:
			self.head=new_node
		else:
			new_node.right=self.head
			self.head.left=new_node
			self.head=new_node
			print(data,"is added at begin..")
		

	def addAtAfter(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		key=int(input("Enter data after which data will be added: "))

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.right is not None:
				if key==ptr.data:
					break
				else:
					ptr=ptr.right
			if ptr.right is None:
				print(key," not found ")
			else:
				ptr1=ptr.right
				new_node.right=ptr1
				ptr1.left=new_node
				ptr.right=new_node
				new_node.left=ptr
				print(data,"is added after ",key)

	def addAtBefore(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		key=int(input("Enter data after which data will be added: "))

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.right is not None:
				if key==ptr.data:
					break
				else:
					ptr=ptr.right
			if ptr.right is None:
				print(key," not found ")
			else:
				ptr1=ptr.left
				new_node.right=ptr
				ptr.left=new_node
				ptr1.right=new_node
				new_node.left=ptr1
				print(data,"is added before ",key)


	def addAtEnd(self):
		data=int(input("Enter data: "))
		new_node=GetNode(data)
		#new_node.data=data

		if self.head is None:
			self.head=new_node
		else:
			ptr=self.head
			while ptr.right is not None:
				ptr=ptr.right
			ptr.right=new_node
			new_node.left=ptr
			print(data,"is added at the end..")

	def deleteAtBegin(self):
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			ptr1=ptr.right
			ptr.right=None
			self.head=ptr1
			print(ptr.data,"is deleted from begin..")

	def deleteAtAfter(self):
		key=int(input("Enter data after which data will be added: "))

		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.right is not None:
				if key==ptr.data:
					break
				else:
					ptr=ptr.right
			if ptr.right is None:
				print(key," not found ")
			else:
				ptr1=ptr.right
				ptr2=ptr1.right
				ptr.right=ptr2
				ptr2.left=ptr
				ptr1.right=None
				print(ptr1.data," is deleted after ",key)
	

	def deleteAtValue(self):
		key=int(input("Enter data which node will be deleted: "))

		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.right is not None:
				if key==ptr.data:
					break
				else:
					ptr=ptr.right
			if ptr.right is None:
				print(key," not found ")
			else:
				ptr1=ptr.left
				ptr2=ptr.right
				ptr1.right=ptr2
				ptr2.left=ptr1
				ptr.right=None
				print(ptr.data,"is deleted at ",key)



	def deleteAtEnd(self):
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr.right is not None:
				ptr=ptr.right
			ptr1=ptr.left
			ptr1.right=None
			print(ptr.data,"is deleted from the end..")	

	def length(self):
		len=0
		if self.head is None:
			print("LinkedList is empty..")
		else:
			ptr=self.head
			while ptr is not None:
				len=len+1
				ptr=ptr.right
			print("Size of LinkedList is ",len)

obj=LinkedList()
if __name__ == '__main__':
	while True:
		print("\n\n1. Append\t\t2. Add At Begin  \t3. Add At After")
		print("4. Add At Before\t5. Add At End\t\t6. Delete At Begin")
		print("7. Delete At After\t8. Delete Ay Node\t9. Delete At End")
		print("10. Length\t\t11. TraverseForward\t12. TraverseBackward \n0. Exit")
		n=int(input("Select your choice: "))
		if n==1:
			obj.append()
		elif n==2:
			obj.addAtBegin()
		elif n==3:
			obj.addAtAfter()
		elif n==4:
			obj.addAtBefore()
		elif n==5:
			obj.addAtEnd()
		elif n==6:
			obj.deleteAtBegin()
		elif n==7:
			obj.deleteAtAfter()
		elif n==8:
			obj.deleteAtValue()
		elif n==9:
			obj.deleteAtEnd()
		elif n==10:
			obj.length()
		elif n==11:
			obj.traverseForward()
		elif n==12:
			obj.traverseBackward()
		elif n==0:
			sys.exit()





