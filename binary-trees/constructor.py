# create global class to create Node 
# setting next => None means there is no link or end of list

# root node init
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        # each node needs to have something pointing to it
        self.root = None

    # create insert method 
    # create new node
    # if root is None => new_node
    # set temp var to root 
    # while loop since len(n) is unknown
    # if new_node == temp return false
    # if < left else > right
    # if None insrt new_node else move to next node 


    def insert(self, value):
        # creat a node
        new_node = Node(value)

        # edge case with empty tree
        if self.root is None:
            self.root = new_node
            # if insert at root then don't continue running code at this method
            return True

        # create start var
        temp = self.root

        while (True):
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

        # find a value in the tree
        # if root == None return False
        # temp == self.root
        # while temp is not None 
        
    def contains(self, value):
            # if self.root == None:
            #     return False
            temp = self.root

            while temp is not None:
                if value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
                else:
                    return True
            return False

    # recursion 
    # def minVal(self, node):
    #     while node.left is not None:
    #         node = node.left
    #     return node.value

    # edge case when you need to get left minVal
    def getLeftMost(x):
        while (x.left is not None):
            return x.left
        return getLeftMost(x.left)
    
    # if you have to go up
    # check if tree exists
    # check node.right == current_node
    # if upperNode > currentNode.left: return 
    
    # if you have to go down
    # check node.right exits:
    # check if node.left exists:
    # continue down node.left until empty

# remove node in BST
 # if node to delete has 1 child 
        # relink child.left/righth to child.parent

        # if node to delete has 2 child or root node
        # successor = minVal in right subtree 

# if you want to remove root you need to replae with minVal of right subtree (in order succcesor)
#
def getLeftMost(self):
    while self.left != None:
            return self
    return getLeftMost(self.left)

# check root node
def deleteNode(self, inputNode):
    if self.root is None:
        # then we have no element to delete
        return rootNode.root

    if inputNode < self.root:
        self.left = deleteNode(self.left, inputNode)
    elif inputNode > self:
            self.right = deleteNode(self.root.right, inputNode)
    
    else:
        if self.left is None:
            temp = self.left
            self = None
            return temp

        if self.right is None:
            temp = self.right
            rootNode = None
            return temp
        
        # node has two children
        # find minVal succesor 
        temp = getLeftMost(self.right)
        self.value = temp.value
        # delete minVal of right subtree
        self.right = deleteNode(self.right, temp.value)

    return self

my_tree = BinarySearchTree()
my_tree.insert(70)
my_tree.insert(50)
my_tree.insert(90)
my_tree.insert(30)
my_tree.insert(60)
my_tree.insert(80)
my_tree.insert(100)
my_tree.insert(20)
my_tree.insert(40)

print(my_tree.contains(100))
# print(my_tree.contains(17))
# print(BinarySearchTree.getLeftMost(BinarySearchTree.root))
# print(BinarySearchTree.getLeftMost(BinarySearchTree.root.right))

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
