class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        # create a queue
        queue = []
        queue.append([start])
        
        while queue:
            # first path from queue
            path = queue.pop(0)
            # get last node from path 
            node = path[-1]
            if node == end:
                return path
            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)

custDict = { 'A' : ['A', 'C','D'],
  'B': ['A','E'],
  'C': ['A','F'],
  'D': ['A','G'],
  'E': ['B','G'],
  'G': ['D','E','F'],
  'F': ['C','G']
  }               

g = Graph(custDict)
print(g.bfs('A', 'F'))

