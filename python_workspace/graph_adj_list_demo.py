#class to represent the adjacency list of the node
class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None

#class to represent graph
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V

    #function to add an edge in undireced graph
    def add_edge(self,src,dest):
        #adding node to source node
        node = AdjNode(dest)
        node.next=self.graph[src]
        self.graph[src]=node

        #adding source node to destination
        node=AdjNode(src)
        node.next=self.graph[dest]
        self.graph[dest]=node

    #functon to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i),end="")
            temp=self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex),end="")
                temp=temp.next
            print(" \n")

V=5
graph=Graph(V)
graph.add_edge(0,1)
graph.add_edge(0,4)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(1,4)
graph.add_edge(2,3)
graph.add_edge(3,4)

graph.print_graph()