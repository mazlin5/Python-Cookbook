# vertices(vertex) : vertices are the nodes of the graph 
# edge -  line that connects pairs of vertices
# unweighted graph - graph which does not have a weight assoc w any edge
# undirected graph - do not have direction assoc w/ them - can access everything
# directed graph - have direction associated by arrows 
# cyclic graph - has atleast one loop 
# acyclic graph - has no loop but cannot travel all vertices
# tree - special case of directed acyclic graphs 

# Representation 
# --------------
# adjancency matrix - sqaure matrix or 2D array. elements of matrix
# indicate whether pairs of vertices are adjacent or not

# 2D Array -  5X5 init at 0
#  each edge or connection = 1 in 2D array, vertices can never connect to itself


#*** using linked-list representation ********
# ['A','B','C','D','E'] - > connection nodes 

class Graph:
    def __init__(self, gdict=None):
        # if empty create graph
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addVertex(self, inputVertex):

        # check if vertex already exists
        if inputVertex not in self.gdict.keys():
            self.gdict[inputVertex] = []
        else:
            None
    
    def addEdge(self, vertex, edge):
            self.gdict[vertex].append(edge)
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].removeEdge(vertex2)
            self.gdict[vertex2].removeEdge(vertex1)
        # remove everywhere 
        return False

    # vertex is the node you want to start from for traversal 
    def bfs(self, vertex):
        # create list to track visited nodes
        visited = [vertex]
        queue = [vertex]

        # begining traversal since started at exisiting vertices
        while queue: #o(v)
            # FIFO methodology 
            deVertex = queue.pop(0) #{ 'A' : }
            print(deVertex)
            # do this step for # of edge times
            for adjacentVertex in self.gdict[deVertex]:
                # print(adjacentVertex)
                if adjacentVertex not in visited:
                    # o(1)
                    visited.append(adjacentVertex)
                    # # end our queue with adjacent vertex
                    queue.append(adjacentVertex)
                return visited
        # .pop(0) dequeeue visited elements 

# given edge, go as deep as possible, once done, backtrack
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while (stack):  #o(v)
            # pulls last element 
            popVer = stack.pop()
            print(popVer)
            # check for adjacent vertices
            for adj in self.gdict[popVer]:
                if adj not in visited:
                    visited.append(adj)
                    stack.append(adj)


custDict = { 'A' : ['B', 'C'],
  'B': ['A','D','E'],
  'C': ['A','E'],
  'D': ['B','E'],
  'E': ['D','F'],
  'F': ['E', 'E']
  }

m = Graph(custDict)
# print(m.gdict)
# m.addVertex("G")
# m.addEdge("G","F")
# print(m.gdict)
m.dfs("A")
# print(m.gdict)

