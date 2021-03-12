from collections import defaultdict

#class representing a directed graph
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    #function to add edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    #function to print a BFS of graph
    def BFS(self,start):
        #mark all vertices as not visited
        visited=[False]*(max(self.graph)+1)
        #createa queue for BFS
        queue=[]
        #mark source node as visisted and enqueue it
        queue.append(start)
        visited[start]=True
        
        while queue:
            #dequeue a vertex from queue and print it
            start = queue.pop(0)
            print(start,end=" ")
            #get all adjacent vertices of the dequeued vertex start
            #if adjacent has not been visisted,
            #then mark it visited and enqueue it
            for i in self.graph[start]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)