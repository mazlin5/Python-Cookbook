# Given {'a': ['1'],  "ab": "12" --> data = '12 or "l" 
#        'b': ['2'],     return 2
#        'c': ['3'] 
#       }
#           }
# Ex. nun_ways(data)

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # traverse a tree using levelOrder of tree 
    def levelOrder(root):
        queue = [root]

        while queue:
            elim = queue.pop(0)
            if elim:
                print(elim.value, end=' ')
                queue.append(elim.left)
                queue.append(elim.right)
                
            