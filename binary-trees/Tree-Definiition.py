# Given a BST and target, return the value closes to target 
# node.right must be > than node.left - traverse entire 
# keep track of target value that allows confirmation > that current closest

# what are the advantages and disadvantages of solving this iteratively vs recursively 


# start of with simple class def

class BinaryNode:
    def __init__(self, value):
        self.value = value
        # reference other intance of BTS
        self.left = None
        self.right = None
    
    def insertL(self, newNode):
        if self.left is None:
            # add node to tree
            self.left = BinaryNode(newNode)
        # if there is already a left node.. create new node below
        else:
            t = BinaryNode(newNode)
            t.left = self.left
            self.left = t

    def insertR(self, newNode):
        if self.right is None:
            # add node to tree
            self.right = BinaryNode(newNode)
        # if there is already a left node.. create new node below
        else:
            t = BinaryNode(newNode)
            # don't overwrite something before you set it
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right.value
        
    def getLeftChild(self):
        return self.left.value

    # set root node 
    def setRoot(self,value):
        self.value = value
        
    # get root node
    def getRoot(self):
        return self.value

r = BinaryNode(10)
print(r.getRoot())
r.setRoot(12)
# print('New root node: ',r.getRoot())
r.insertL(13)
r.insertR(14)
print(r.getLeftChild())
print(r.getRightChild())



