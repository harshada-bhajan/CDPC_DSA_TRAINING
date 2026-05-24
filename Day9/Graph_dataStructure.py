#Implementation of Graph Data Structure
import sys


class Graphs:

    def __init__(self):
        self.nodes = []
        self.graph = []
        self.nodeCount = 0

    def addnode(self, v):

        if v in self.nodes:
            print(v, "is already present")

        else:
            self.nodeCount += 1
            self.nodes.append(v)

            for x in self.graph:
                x.append(0)

            temp = []

            for x in range(self.nodeCount):
                temp.append(0)

            self.graph.append(temp)

            print(v, "is added")

    def addedge_undirected_unweighted(self, v1, v2):

        if v1 not in self.nodes:
            print(v1, "not present")
            return

        if v2 not in self.nodes:
            print(v2, "not present")
            return

        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)

        self.graph[index1][index2] = 1
        self.graph[index2][index1] = 1

        print("Edge added successfully")

    def addEdge_undirected_weighted(self,v1,v2,weight):
        if v1 not in self.nodes:
            print(v1, "not present")
            return

        if v2 not in self.nodes:
            print(v2, "not present")
            return

        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)

        self.graph[index1][index2] = weight
        self.graph[index2][index1] = weight

        print("Edge added successfully")
        

    def addnode_Directed_weighted(self,v1,v2,weight):
        if v1 not in self.nodes:
            print(v1, "not present")
            return

        if v2 not in self.nodes:
            print(v2, "not present")
            return

        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)

        self.graph[index1][index2] = weight
        

        print("Edge added successfully")

    def printGraph(self):

        print(*self.nodes)

        for i in range(self.nodeCount):

            for j in range(self.nodeCount):
                print(self.graph[i][j], end=" ")

            print()

    def deletenode(self,v):
        if v not in self.nodes:
            print(v,"not present")
        else:
            self.nodeCount-=1
            index1=self.nodes.index(v)
            self.nodes.pop(index1)
            self.graph.pop(index1)
            for x in self.graph:
                x.pop(index1)
            print(v, "is deleted")


obj = Graphs()

while True:

    print("\n1. (Insertion) add a node using adjacency matrix representation")
    print("2. (Insertion) add a edge using adjacency matrix representation")
    print("3. (Insertion) add a edge using undirected weighted graph")
    print("4. (Insertion) add a node using directed weighted graph")
    print("5. Print Graph")
    print("6. Delete Operation")
    print("0. Exit\n")

    n = int(input("Enter any choice :"))

    if n == 1:

        v = input("Enter vertex: ")
        obj.addnode(v)

    elif n == 2:

        v1 = input("Enter vertex1: ")
        v2 = input("Enter vertex2: ")

        obj.addedge_undirected_unweighted(v1, v2)

    elif n == 3:
        v1 = input("Enter vertex1: ")
        v2 = input("Enter vertex2: ")
        weight = input("Enter weight: ")
        obj.addEdge_undirected_weighted(v1, v2, weight)

    elif n == 4:
        v1 = input("Enter vertex1: ")
        v2 = input("Enter vertex2: ")
        weight = input("Enter weight: ")
        obj.addnode_Directed_weighted(v1, v2, weight)

    elif n == 5:

        obj.printGraph()

    elif n == 6:
        v = input("Enter vertex to Delete: ")
        obj.deletenode(v)

    elif n == 0:

        sys.exit()
